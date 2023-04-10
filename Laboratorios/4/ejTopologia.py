
import sys
import os

from pyomo.environ import *
from pyomo.opt import SolverFactory

import math
import matplotlib.pyplot as plt

#os.system("cls")

Model = ConcreteModel()

# ================= #
# SETS & PARAMETERS #
# ================= #

N = RangeSet(1, 7)
C = Set(initialize=['x', 'y'])

conexionesRaw = {
                    (1, 'x'): 20, (1, 'y'): 6,
                    (2, 'x'): 22, (2, 'y'): 1,
                    (3, 'x'): 9, (3, 'y'): 2,
                    (4, 'x'): 2, (4, 'y'): 25,
                    (5, 'x'): 21, (5, 'y'): 10,
                    (6, 'x'): 29, (6, 'y'): 2,
                    (7, 'x'): 14, (7, 'y'): 12
                }

conexiones = {}

for i in N:
    for j in N:
        d = math.sqrt((conexionesRaw[(i, 'x')] - conexionesRaw[(j, 'x')]) ** 2 + (conexionesRaw[(i, 'y')] - conexionesRaw[(j, 'y')]) ** 2)
        if d <= 20 and d > 0:
            conexiones[(i, j)] = d;
        elif d == 0:
            conexiones[(i, j)] = 999
        else:
            conexiones[(i, j)] = 999
            
# ========= #
# VARIABLES #
# ========= #

Model.x = Var(N, N, domain=Binary)

# ================== #
# OBJECTIVE FUNCTION #
# ================== #

Model.z = Objective(expr=sum(conexiones[(i, j)] * Model.x[i, j] for i in N for j in N))

# =========== #
# CONSTRAINTS #
# =========== #

nodo_origen = 4
nodo_destino = 6

def restrNodoOrigen(Model, i):
    if i == nodo_origen:
        return sum(Model.x[i, j] for j in N) == 1
    else:
        return Model.Skip
    
Model.restrNodoOrigen = Constraint(N, rule=restrNodoOrigen)

def restrNodoDestino(Model, j):
    if j == nodo_destino:
        return sum(Model.x[i, j] for i in N) == 1
    else:
        return Model.Skip
    
Model.restrNodoDestino = Constraint(N, rule=restrNodoDestino)

def restrNodoInter(Model, i):
    if i != nodo_origen and i != nodo_destino:
        return sum(Model.x[i, j] for j in N) - sum(Model.x[j, i] for j in N) == 0
    else:
        return Model.Skip
    
Model.restrNodoInter = Constraint(N, rule=restrNodoInter)

# =================== #
# APPLYING THE SOLVER #
# =================== #

SolverFactory('glpk').solve(Model)

Model.display()

# ===== #
# GRAPH #
# ===== #

values = {}

for i in Model.x:
    if Model.x[i].value != 0.0:
        values[i] = Model.x[i].value

plt.figure(1)

# Puntos
for i in N:
    plt.plot([conexionesRaw[i, 'x']], [conexionesRaw[i, 'y']], 'ok')
    plt.annotate(str(i), (conexionesRaw[i, 'x'], conexionesRaw[i, 'y']), textcoords="offset points", xytext=(0, 10), ha='center')
    
# Líneas
for i, j in conexiones:
    if conexiones[(i, j)] != 999 and conexiones[(i, j)] is not None:
        if (i, j) in values: # Camino más corto
            plt.plot([conexionesRaw[i, 'x'], conexionesRaw[j, 'x']], [conexionesRaw[i, 'y'], conexionesRaw[j, 'y']], color='r', linewidth=3)
        else:
            if (j, i) not in values: # estaba pintando (7, 4) por alguna razón...
                plt.plot([conexionesRaw[i, 'x'], conexionesRaw[j, 'x']], [conexionesRaw[i, 'y'], conexionesRaw[j, 'y']], linestyle='dashed', color='black', linewidth=1)

plt.show()
