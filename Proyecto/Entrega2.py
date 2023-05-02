import pyomo.environ as pyo
from pyomo.environ import *

Model = ConcreteModel()
murales_disponibles = 3
refrescos_disponibles = 2
deseados = 1
enlaces = 3
nodos_totales = 6
tipos_nodos = 3

Model.tipo_nodos = RangeSet(tipos_nodos)
Model.totales = RangeSet(nodos_totales)
Model.murales= RangeSet(murales_disponibles)
Model.deseados= RangeSet(deseados)
Model.refrescos = RangeSet(refrescos_disponibles)
Model.enlacesR = RangeSet(enlaces)
# Nomenclatura tablas de identificación de nodos
# dentro del conjunto N la nomenclaura será la siguiente
# Nodo inicial ( el tipo "hotel" = 1) 0 
# Nodos murales (el tipo "mural" = 2) [1,2,3]
# Nodos murales (el tipo "Refrescos" = 3) [4,5]
# filas de 1-3 
# Columnas 0-8 
# en la matriz 8*3 donde en las columnas los hay booleanos para el tipo (un 1 en la columna 0 significa que es el hotel y asi)
matriz_tipo_nodos= [
    [1,0,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,0,1],
    [0,0,1]
]

Model.matriz_nodos = Param(Model.totales, Model.tipo_nodos, initialize=lambda Model, k, l: matriz_tipo_nodos[k-1][l-1], mutable=True)

matriz_costos = [
    # H M1 M2 M3 R1 R2
    [0,2,5,5,1,9], # Hotel
    [2,0,3,5,2,10], # Mural 1
    [5,3,0,2,3,11], # Mural 2
    [5,5,2,0,4,12], # Mural 3
    [1,2,3,4,0,13], # Refresco 1
    [9,10,11,12,13,0] # Refresco 2
]

Model.matriz_costos = Param(Model.totales, Model.totales, initialize=lambda Model, i, j: matriz_costos[i-1][j-1], mutable=True)

Model.x = Var(Model.totales, within=Binary) # variable que determina si un nodo es visitado o no
#variable binaria que determina la selección de un enlace
Model.y = Var(Model.totales, Model.totales, Model.enlacesR ,within=Binary)

#TSP
def objective_rule(Model):
    return sum(Model.matriz_costos[i,j]*Model.x[i] for i in Model.totales for j in Model.totales)

def restriccion_murales(Model, murales_deseados):
    return sum(Model.matriz_nodos[i,1] * Model.x[i] for i in Model.totales) == murales_deseados

# restricción de que solo se puede visitar un nodo refresco, es decir que la matriz en la columna 3 solo puede tener un 1
def solo_un_refresco(Model):
    return sum(Model.matriz_nodos[i,3] * Model.x[i] for i in Model.totales) == 1

#restriccion que dice si solo se puede visitar un enlace de un nodo a otro 
def restriccion_enlaces(Model):
    return sum(Model.y[i] for i in Model.totales) + sum(Model.y[i] for i in Model.totales ) <= 1

def restr2_rule(Model, k):
    return sum(Model.x[i, j, k] for i in Model.totales for j in Model.totales) == 1

def restr3_rule(Model,i,j):
    return sum(Model.y[i,j,k] for k in Model.enlacesR) <= 1

def restr4_rule(Model,i):
    return sum(Model.y[i,j,k] for j in Model.totales for k in Model.enlacesR) <= 1

def restr5_rule(Model,j):
    return sum(Model.y[i,j,k] for i in Model.totales for k in Model.enlacesR) <= 1


Model.obj = Objective(rule=objective_rule, sense=minimize)
Model.restriccion_murales = Constraint(Model.deseados, rule=restriccion_murales)
Model.solo_un_refresco = Constraint(rule=solo_un_refresco)
Model.restriccion_enlaces = Constraint(rule=restriccion_enlaces)
Model.restr2 = Constraint(Model.totales, rule=restr2_rule)
Model.restr3 = Constraint(Model.totales, Model.totales, rule=restr3_rule)
Model.restr4 = Constraint(Model.totales, rule=restr4_rule)
Model.restr5 = Constraint(Model.totales, rule=restr5_rule)

#Model.obj = Objective(expr=sum(Model.matriz_costos[i,j]*Model.x[i] for i in Model.totales for j in Model.totales), sense=minimize)





