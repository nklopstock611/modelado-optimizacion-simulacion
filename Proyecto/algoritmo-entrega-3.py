from itertools import permutations

def generate_path_permutations(graph, num_murals, num_parques, num_hoteles):
    # Obtener los nodos del grafo por tipo
    parks = [node for node in graph if node.type == "parque"]
    murals = [node for node in graph if node.type == "mural"]
    hotel = [node for node in graph if node.type == "hotel"][0]  # Asumimos que solo hay un nodo tipo hotel

    # Generar todas las permutaciones posibles de los murales
    mural_permutations = permutations(murals)
    
    # Generar todas las permutaciones posibles de los parques
    park_permutations = permutations(parks)
    
    # Generar todas las permutaciones posibles de los caminos
    for mural_permutation in mural_permutations:
        for park_permutation in park_permutations:
            # Construir el camino con el hotel, los murales y el parque
            path = [hotel] + list(mural_permutation) + list(park_permutation)
            path_permutations = permutations(path, num_murals + num_parques + num_hoteles)
            # Devolver la permutación como resultado                
            return path_permutations

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
graph[0].add_connection(graph[0], 2)
graph[2].add_connection(graph[2], 3)
graph[3].add_connection(graph[3], 5)
graph[4].add_connection(graph[4], 1)
graph[5].add_connection(graph[5], 9)

graph[2].add_connection(graph[2], INF)
graph[0].add_connection(graph[0], 5)
graph[1].add_connection(graph[1], 3)
graph[3].add_connection(graph[3], 2)
graph[4].add_connection(graph[4], 3)
graph[5].add_connection(graph[5], 11)

graph[3].add_connection(graph[3], INF)
graph[0].add_connection(graph[0], 5)
graph[1].add_connection(graph[1], 5)
graph[2].add_connection(graph[2], 2)
graph[4].add_connection(graph[4], 4)
graph[5].add_connection(graph[5], 12)

graph[4].add_connection(graph[4], INF)
graph[0].add_connection(graph[0], 2)
graph[1].add_connection(graph[1], 2)
graph[2].add_connection(graph[2], 3)
graph[3].add_connection(graph[3], 4)
graph[5].add_connection(graph[5], 4)

graph[5].add_connection(graph[5], INF)
graph[0].add_connection(graph[0], 6)
graph[1].add_connection(graph[1], 2)
graph[2].add_connection(graph[2], 3)
graph[3].add_connection(graph[3], 6)
graph[4].add_connection(graph[4], 4)

num_murals = 3 #len([node for node in graph if node.type == "mural"])
num_parques = 1 #len([node for node in graph if node.type == "parque"])
num_hoteles = 1
path_permutations = list(generate_path_permutations(graph, num_murals, num_parques, num_hoteles))

# for path in path_permutations:
#     for node in path:
#         print(node.id)
#     print()

def valid_permutations(permutations):
    # toca recorrer cada arreglo de permutaciones y verificar
    # cuales permutaciones son válidad según las conexiones.
    for path in path_permutations:
        for node in path:
            print(node.connections)
        print()

print(valid_permutations(path_permutations))

def get_path_costs(permutation):
    # toca recorrer cada arreglo de permutaciones válidas
    # y calcular el camino más corto entre todos.
    pass

def min_cost_path(permutations):
    # toca sacar el costo de cada arreglo de permutaciones
    # y encontrar el mínimo mínimo.
    pass
