import pyomo.environ as pyo
from pyomo.environ import *

Model = ConcreteModel()

cant_losas = 20
cant_tubos = 7

Model.losas= RangeSet(cant_losas)
Model.tubos = RangeSet(cant_tubos)

matriz_values = [    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1]
]

Model.matriz = Param(Model.tubos, Model.losas, initialize=lambda Model, i, j: matriz_values[i-1][j-1], mutable=True)

#vars
Model.x= Var(Model.losas, domain=Binary)
Model.obj = Objective(expr=sum(Model.x[j] for j in Model.losas), sense=minimize)

#restricciones
def restriccion_tubos(Model, i):
    return sum(Model.matriz[i,j]*Model.x[j] for j in Model.losas) >= 1

Model.restriccion_tubos = Constraint(Model.tubos, rule=restriccion_tubos)

# create an instance of the model
instance = Model.create_instance()

# solve the instance
solver = SolverFactory('glpk')
solver.solve(instance)
instance.display()
# print the results
for j in instance.losas:
    print(f"x[{j}] = {pyo.value(instance.x[j])}")




