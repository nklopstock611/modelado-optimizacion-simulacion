
import sys
import os

from pyomo.environ import *
from pyomo.opt import SolverFactory

#os.system("cls")

Model = ConcreteModel()

# ================= #
# SETS & PARAMETERS #
# ================= #

inf_range = 1
sup_range = 6

N = RangeSet(inf_range, sup_range)

tiempo = {}

for i in N:
    for j in N:
        tiempo[(i, j)] = 0
        
valores = [0, 10, 20, 30, 30, 20,
           10, 0, 25, 35, 20, 10,
           20, 25, 0, 15, 30, 20,
           30, 35, 15, 0, 15, 25,
           30, 20, 30, 15, 0, 14,
           20, 10, 20, 25, 14, 0]

for i, each in enumerate(tiempo):
    tiempo[each] = valores[i]

conexiones = {}

for i in N:
    for j in N:
        if tiempo[(i, j)] <= 15:
            conexiones[(i, j)] = 1
        elif tiempo[(i, j)] > 15:
            conexiones[(i, j)] = 0
            
# ========= #
# VARIABLES #
# ========= #

Model.x = Var(N, domain=Binary)

# ================== #
# OBJECTIVE FUNCTION #
# ================== #

Model.z = Objective(expr=sum(Model.x[i] for i in N))

# =========== #
# CONSTRAINTS #
# =========== #

def zonas(Model, j):
    return sum(conexiones[(i, j)] * Model.x[i] for i in N) >= 1

Model.zonas = Constraint(N, rule=zonas)

# =================== #
# APPLYING THE SOLVER #
# =================== #

SolverFactory('glpk').solve(Model)

Model.display()  