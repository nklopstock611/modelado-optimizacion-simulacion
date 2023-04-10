import pyomo.environ as pyo
from pyomo.environ import *

Model = ConcreteModel()
numOrigen = 3 
numDestino = 2
numProcesos = 2

# definicion de sets en pyomo
Model.origen = RangeSet(numOrigen)
Model.destino = RangeSet(numDestino)
Model.tipo_procesos = RangeSet(numProcesos)

# definicion de parametros en pyomo
Model.costos=Param(Model.origen, Model.destino, mutable=True)
Model.costos[1,1]= 300
Model.costos[1,2]= 500
Model.costos[2,1]= 200
Model.costos[2,2]= 300
Model.costos[3,1]= 600
Model.costos[3,2]= 300

Model.cantOrigen=Param(Model.origen, Model.tipo_procesos, mutable=True)
Model.cantOrigen[1,1]= 60
Model.cantOrigen[1,2]= 80
Model.cantOrigen[2,1]= 80
Model.cantOrigen[2,2]= 50
Model.cantOrigen[3,1]= 50
Model.cantOrigen[3,2]= 50

Model.cantDestino=Param(Model.destino, Model.tipo_procesos, mutable=True)
Model.cantDestino[1,1]= 100
Model.cantDestino[1,2]= 60
Model.cantDestino[2,1]= 90
Model.cantDestino[2,2]= 120

# definicion de variables en pyomo
Model.x=Var(Model.origen, Model.destino, Model.tipo_procesos, domain=NonNegativeReals)
Model.obj = Objective(expr = sum(Model.costos[i,j]*Model.x[i,j,k] for i in Model.origen for j in Model.destino for k in Model.tipo_procesos), sense=minimize)

# definicion de restricciones en pyomo
def cantOrigen_rule(Model, i, k):
    return sum(Model.x[i,j,k] for j in Model.destino) == Model.cantOrigen[i,k]

Model.origen_rule = Constraint(Model.origen, Model.tipo_procesos, rule=cantOrigen_rule)

def cantDestino_rule(Model, j, k):
    return sum(Model.x[i,j,k] for i in Model.origen) == Model.cantDestino[j,k]

Model.destino_rule = Constraint(Model.destino, Model.tipo_procesos, rule=cantDestino_rule)
solver = SolverFactory('glpk')
results = solver.solve(Model)
Model.display()

print(f"Optimal Solution: {Model.obj():,.2f}")
for i in Model.origen:
    for j in Model.destino:
        for k in Model.tipo_procesos:
            if Model.x[i,j,k]() > 0:
                print(f"x[{i},{j},{k}] = {Model.x[i,j,k]():,.2f}")