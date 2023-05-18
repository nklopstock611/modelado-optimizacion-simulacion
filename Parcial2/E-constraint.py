from pyomo.environ import *
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt

def delete_component(Model, comp_name):

        list_del = [vr for vr in vars(Model)
                    if comp_name == vr
                    or vr.startswith(comp_name + '_index')
                    or vr.startswith(comp_name + '_domain')]

        list_del_str = ', '.join(list_del)
        print('Deleting model components ({}).'.format(list_del_str))

        for kk in list_del:
            Model.del_component(kk)

# Definicion de parametros + nodos de origen y destino
Modelo = ConcreteModel()
cant_nodos = 5
o = 1
d = 5
epsilon = 5
# Tabla de Hops
Modelo.nodos = RangeSet(1, cant_nodos)
Modelo.hops = Param(Modelo.nodos, Modelo.nodos, mutable=True)

for i in Modelo.nodos:
    for j in Modelo.nodos:
        Modelo.hops[i, j] = 999

Modelo.hops[1, 2] = 1
Modelo.hops[1, 3] = 1
Modelo.hops[2, 5] = 1
Modelo.hops[3, 4] = 1
Modelo.hops[4, 5] = 1

# Tabla de costos
Modelo.costos = Param(Modelo.nodos, Modelo.nodos, mutable=True)

for i in Modelo.nodos:
    for j in Modelo.nodos:
        Modelo.costos[i, j] = 999

Modelo.costos[1, 2] = 10
Modelo.costos[1, 3] = 5
Modelo.costos[2, 5] = 10
Modelo.costos[3, 4] = 5
Modelo.costos[4, 5] = 5

# Definicion de variables
# Variable de decision x_ij
Modelo.x = Var(Modelo.nodos, Modelo.nodos, domain=Binary)

# Funciones objetivo
Modelo.fo1 = sum(Modelo.x[i, j] * Modelo.hops[i, j] for i in Modelo.nodos for j in Modelo.nodos)
Modelo.fo2 = sum(Modelo.x[i, j] * Modelo.costos[i, j] for i in Modelo.nodos for j in Modelo.nodos)

epsilon = 5
unfeasible = False
sol_f1 = []
sol_f2 = []
while epsilon > -1:

    Modelo.o_Z = Objective(expr=Modelo.fo2)

    # Define the source node constraint
    def source_node_rest(model, i):
        if i == model.nodos[1]:
            return sum(model.x[i, j] for j in model.nodos) == 1
        else:
            return Constraint.Skip

    # Define the intermediate node constraint
    def intermediate_node_rest(model, i):
        if i != model.nodos[1] and i != model.nodos[5]:
            return sum(model.x[i, j] for j in model.nodos) - sum(model.x[j, i] for j in model.nodos) == 0
        else:
            return Constraint.Skip

    # Define the destination node constraint
    def destination_node_rest(model, j):
        if j == model.nodos[5]:
            return sum(model.x[i, j] for i in model.nodos) == 1
        else:
            return Constraint.Skip

    # Define the f1 constraint
    def f1_constraint_rule(model):
        return model.fo1 <= epsilon
    
    epsilon -=1

    # Apply the constraints to the model
    Modelo.source = Constraint(Modelo.nodos, rule=source_node_rest)
    Modelo.intermediate = Constraint(Modelo.nodos, rule=intermediate_node_rest)
    Modelo.destination = Constraint(Modelo.nodos, rule=destination_node_rest)
    Modelo.f1Constraint = Constraint(rule=f1_constraint_rule)
    solver = SolverFactory('glpk')  
    # Solve the optimization problem
    results = solver.solve(Modelo)

    valorF1=value(Modelo.fo1)
    valorF2=value(Modelo.fo2)
    sol_f1.append(valorF1)
    sol_f2.append(valorF2)
    
    delete_component(Model, 'o_z')
    delete_component(Model, 'source')
    delete_component(Model, 'destination')
    delete_component(Model, 'intermediate')
    delete_component(Model, 'f1Constraint')

plt.plot(sol_f1,sol_f2,'o-.');
plt.title('Frente Optimo de Pareto');
plt.xlabel('F1')
plt.ylabel('F2')

plt.grid(True);
plt.show()


