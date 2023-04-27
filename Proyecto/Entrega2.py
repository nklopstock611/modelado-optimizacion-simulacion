import pyomo.environ as pyo
from pyomo.environ import *

Model = ConcreteModel()
murales_disponibles = 5
deseados = 3

Model.murales= RangeSet(murales_disponibles)
Model.deseados= RangeSet(deseados)

