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

Model.matriz_nodos = Param(Model.totales, Model.tipo_nodos, initialize=lambda Model, i, j: matriz_tipo_nodos[i-1][j-1], mutable=True)

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

Model.x = Var(Model.totales, within=Binary)
Model.y = Var(Model.totales, Model.tipo_nodos, within=Binary)

Model.obj = Objective(expr=sum(Model.matriz_costos[i,j]*Model.x[i] for i in Model.totales for j in Model.totales), sense=minimize)
# se desea recorrer 1 mural
Model.restriccion1 = Constraint(expr=sum(Model.y[i,2] for i in Model.totales) == 1)
# se desea recorrer 1 refresco
Model.restriccion2 = Constraint(expr=sum(Model.y[i,3] for i in Model.totales) == 1)

#se debe salir y llegar al hotel
Model.restriccion3 = Constraint(expr=sum(Model.y[i,1] for i in Model.totales) == 2)





