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

graph = [
    Node(5, "parque"),
    Node(2, "mural"),
    Node(3, "mural"),
    Node(4, "mural"),
    Node(1, "hotel"),
    Node(6, "mural"),
    Node(7, "parque")
]

graph[1].add_connection(graph[2], 3)  # Conexión entre mural 2 y mural 3 con peso 3
graph[2].add_connection(graph[4], 2)  # Conexión entre mural 3 y parque 5 con peso 2
graph[3].add_connection(graph[5], 4)  # Conexión entre mural 4 y parque 5 con peso 4

num_murals = 3 #len([node for node in graph if node.type == "mural"])
num_parques = 1 #len([node for node in graph if node.type == "parque"])
num_hoteles = 1
path_permutations = list(generate_path_permutations(graph, num_murals, num_parques, num_hoteles))
for path in path_permutations:
    for node in path:
        print(node.id)
    print()

def valid_permutations(permutations):
    # toca recorrer cada arreglo de permutaciones y verificar
    # cuales permutaciones son válidad según las conexiones.
    pass

def get_path_costs(permutation):
    # toca recorrer cada arreglo de permutaciones válidas
    # y calcular el camino más corto entre todos.
    pass

def min_cost_path(permutations):
    # toca sacar el costo de cada arreglo de permutaciones
    # y encontrar el mínimo mínimo.
    pass
