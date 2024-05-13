# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2016 - Algoritmos y Estructura de Datos
# Cristian Túnnchez - 231359
# Guatemala, 12 de mayo de 2024

import networkx as nx
import matplotlib.pyplot as plt

# Tarea 1
def cargar_rutas(archivo):
    G = nx.Graph()
    with open(archivo, 'r') as f:
        for linea in f:
            ruta = linea.strip().split(',')
            # Eliminar espacios adicionales en los nombres de las estaciones
            G.add_edge(ruta[0].strip(), ruta[1].strip(), weight=int(ruta[2]))
    return G

def dijkstra(G, inicio):
    return nx.single_source_dijkstra_path(G, inicio), nx.single_source_dijkstra_path_length(G, inicio)