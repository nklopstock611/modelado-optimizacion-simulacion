import pyomo.environ as pyo
from pyomo.environ import *

Model = ConcreteModel()
murales_disponibles = 4
refrescos_disponibles = 4
deseados = 2
enlaces = 4
nodos_totales = 9
tipos_nodos = 3

Model.tipo_nodos = RangeSet(tipos_nodos)
Model.totales = RangeSet(nodos_totales)
Model.murales= RangeSet(murales_disponibles)
Model.deseados= RangeSet(deseados)
Model.refrescos = RangeSet(refrescos_disponibles)

# Nomenclatura tablas de identificación de nodos
# dentro del conjunto N la nomenclaura será la siguiente
# Nodo inicial ( el tipo "hotel" = 1) 0 
# Nodos murales (el tipo "mural" = 2) [1.2.3.4]
# Nodos murales (el tipo "Refrescos" = 3) [5.6.7.8]
# filas de 1-3 
# Columnas 0-8 
# en la matriz 8*3 donde en las columnas los hay booleanos para el tipo (un 1 en la columna 0 significa que es el hotel y asi)
matriz_tipo_nodos= [
    [1,0,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,0,1],
    [0,0,1],
    [0,0,1],
    [0,0,1]
]

Model.matriz_nodos = Param(Model.totales, Model.tipo_nodos, initialize=lambda Model, i, j: matriz_tipo_nodos[i-1][j-1], mutable=True)