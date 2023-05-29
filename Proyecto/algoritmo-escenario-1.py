from itertools import permutations

# Definir el grafo
class Node:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.connections = {}
    
    def add_connection(self, node, weight):
        self.connections[node] = weight

INF = float("inf")

graph = [
    Node(1, "hotel"),
    Node(2, "mural"),
    Node(3, "mural"),
    Node(4, "mural"),
    Node(5, "parque"),
    Node(6, "mural"),
]

graph[0].add_connection(graph[0], INF)
graph[0].add_connection(graph[1], 2)
graph[0].add_connection(graph[2], 5)
graph[0].add_connection(graph[3], 5)
graph[0].add_connection(graph[4], 2)
graph[0].add_connection(graph[5], 9)

graph[1].add_connection(graph[1], INF)
graph[1].add_connection(graph[0], 2)
graph[1].add_connection(graph[2], 3)
graph[1].add_connection(graph[3], 5)
graph[1].add_connection(graph[4], 1)
graph[1].add_connection(graph[5], 9)

graph[2].add_connection(graph[2], INF)
graph[2].add_connection(graph[0], 5)
graph[2].add_connection(graph[1], 3)
graph[2].add_connection(graph[3], 2)
graph[2].add_connection(graph[4], 3)
graph[2].add_connection(graph[5], 11)

graph[3].add_connection(graph[3], INF)
graph[3].add_connection(graph[0], 5)
graph[3].add_connection(graph[1], 5)
graph[3].add_connection(graph[2], 2)
graph[3].add_connection(graph[4], 4)
graph[3].add_connection(graph[5], 12)

graph[4].add_connection(graph[4], INF)
graph[4].add_connection(graph[0], 2)
graph[4].add_connection(graph[1], 2)
graph[4].add_connection(graph[2], 3)
graph[4].add_connection(graph[3], 4)
graph[4].add_connection(graph[5], 4)

graph[5].add_connection(graph[5], INF)
graph[5].add_connection(graph[0], 6)
graph[5].add_connection(graph[1], 2)
graph[5].add_connection(graph[2], 3)
graph[5].add_connection(graph[3], 6)
graph[5].add_connection(graph[4], 4)

def generate_path_permutations(graph, num_murales, num_parques, num_hoteles):
    
    # nodos del grafo por tipo
    parks = [node for node in graph if node.type == "parque"]
    murals = [node for node in graph if node.type == "mural"]
    hotel = [node for node in graph if node.type == "hotel"][0] # solo queremos el único hotel
    
    # generar todas las permutaciones para cada tipo de nodo (excepto hotel)
    mural_permutations = permutations(murals)
    park_permutations = permutations(parks)
    
    # generar todas las permutaciones posibles de los caminos
    for mural_permutation in mural_permutations:
        for park_permutation in park_permutations:
            # construir permutaciones de posibles caminos
            path = [hotel] + list(mural_permutation) + list(park_permutation)
            path_permutations = permutations(path, num_hoteles + num_parques + num_murales)
            
            return path_permutations

def valid_permutations(permutations, num_murales, num_parques, num_hoteles):
    # se recorre cada arreglo de permutaciones y se verifica
    # cuáles permutaciones son válidas según las conexiones
    # y cantidad de nodos de cada tipo.
    
    validos = [] # arreglo para guardar las permutaciones válidas
    for path in permutations:
        cont_murals = 0
        cont_parques = 0
        cont_hoteles = 0

        # revisión de cantidad de tipos de nodos
        for node in path:
            if node.type == "mural":
                cont_murals += 1
            elif node.type == "parque":
                cont_parques += 1
            else:
                cont_hoteles += 1
            
        if cont_murals == num_murales and cont_parques == num_parques and cont_hoteles == num_hoteles:
            validos.append(path)
    
    for path in validos:
        for j, act_node in enumerate(path):

            # revisión de existencia de caminos
            if j < len(path) - 1:
                next_node = path[j + 1]
                if next_node not in act_node.connections:
                    break
            elif j == len(path):
                next_node = path[0]
                if next_node not in act_node.connections:
                    break

    return validos
    
def get_path_cost(permutation):
    # se recorre cada arreglo de permutaciones válidas.
    
    cost_path = 0

    for j, act_node in enumerate(permutation):
        if j < len(permutation) - 1:
            next_node = permutation[j + 1]
            cost_path += act_node.connections[next_node]
        elif j == len(permutation) - 1:
            next_node = permutation[0]
            cost_path += act_node.connections[next_node]

    return cost_path

def min_cost_path(permutations):
    # se calcula el costo de cada arreglo de permutaciones
    # y se encuentra el mínimo entre ellos.

    min_cost = INF
    min_path = None

    for path in permutations:
        cost_path = get_path_cost(path)
        if cost_path < min_cost:
            min_cost = cost_path
            min_path = path

    return min_path, min_cost

def print_path(path, cost):
    # imprimir el camino mínimo

    path = path + (path[0],)
    camino = ""
    for node in path:
        camino += str(node.id) + " -> "

    print("Camino: " + camino[:-4])
    print("Costo: " + str(cost))

num_murales = 1 # se quiere ver un mural
num_parques = 1 # se quiere visitar un parque
num_hoteles = 1 # solo hay un hotel
path_permutations = list(generate_path_permutations(graph, num_murales, num_parques, num_hoteles))
valid = valid_permutations(path_permutations, num_murales, num_parques, num_hoteles)
print_path(min_cost_path(valid)[0], min_cost_path(valid)[1])
