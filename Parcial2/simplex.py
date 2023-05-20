"""
max(3x1 + 2x2)
S.A:
    2x_1 + x_2 <= 100
    x_1 + x_2 <= 80
    x_1 <= 40
    x_1 >= 0
    x_2 >= 0
"""

from random import randint
#import numpy as np
#import matplotlib.pyplot as plt

adyancencias = [
                    {(0, 0): [(0, 80), (40, 0)]},
                    {(0, 80): [(0, 0), (20, 60)]},
                    {(20, 60): [(0, 80), (40, 20)]},
                    {(40, 20): [(20, 60), (40, 0)]},
                    {(40, 0): [(0, 0), (40, 20)]}
               ]

def funcion_objetivo(x1: int, x2: int) -> int:
    return 3 * x1 + 2 * x2

def simplex(adyacencias: list) -> tuple:
    maximiza = 0
    centinela = True

    while centinela:
        rand_int = randint(0, len(adyacencias) - 1)
        rand_coords = list(adyacencias[rand_int].keys())[0]
        fo_izq = funcion_objetivo(adyacencias[rand_int][rand_coords][0][0], adyacencias[rand_int][rand_coords][0][1])
        fo_act = funcion_objetivo(rand_coords[0], rand_coords[1])
        fo_der = funcion_objetivo(adyacencias[rand_int][rand_coords][1][0], adyacencias[rand_int][rand_coords][1][1])

        if fo_act >= fo_izq and fo_act >= fo_der:
            maximiza = fo_act
            centinela = False


    return maximiza, rand_coords

print(simplex(adyancencias))

def draw_fiasable_region():
    # Definir las restricciones
    x1 = np.linspace(0, 40, 100)  # Valores de x1 desde 0 hasta 40
    x2_constraint1 = 100 - 2 * x1  # Restricción 2x1 + x2 <= 100
    x2_constraint2 = 80 - x1  # Restricción x1 + x2 <= 80

    # Crear la figura y el gráfico
    fig, ax = plt.subplots()

    # Graficar las restricciones
    ax.plot(x1, x2_constraint1, label='2x1 + x2 <= 100')
    ax.plot(x1, x2_constraint2, label='x1 + x2 <= 80')

    # Rellenar la zona factible
    ax.fill_between(x1, np.minimum(x2_constraint1, x2_constraint2), 0, where=(x1 >= 0) & (x2_constraint1 >= 0) & (x2_constraint2 >= 0), alpha=0.3)

    # Configurar el gráfico
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 100)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('Zona Factible')
    ax.legend()

    # Dibujar los puntos de las coordenadas
    x = [0, 0, 20, 40, 40]
    y = [0, 80, 60, 20, 0]

    plt.scatter(x, y)

    # Mostrar el gráfico
    plt.show()


