# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2016 - Algoritmos y Estructura de Datos
# Cristian Túnnchez - 231359
# Guatemala, 12 de mayo de 2024

import networkx as nx
import matplotlib.pyplot as plt

# Implementación de un sistema que crea un grafo en NetworkX que representa las rutas del archivo rutas.txt
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

# Implementación de la funcionalidad para ver un mapa de posibles destinos desde una estación de salida
def dibujar_grafo(G, inicio):
    pos = nx.shell_layout(G)  # Posiciones de los nodos
    
    # Dibujar los nodos
    nx.draw_networkx_nodes(G, pos)
    
    # Resaltar el nodo de inicio en color verde
    nx.draw_networkx_nodes(G, pos, nodelist=[inicio], node_color='lime')
    
    # Dibujar las aristas
    nx.draw_networkx_edges(G, pos)
    
    # Dibujar las etiquetas debajo de los nodos
    pos_etiquetas = {node: (coord[0], coord[1]-0.1) for node, coord in pos.items()}
    nx.draw_networkx_labels(G, pos_etiquetas)
    
    plt.show()

# Implementación del algoritmo de Dijkstra para encontrar las mejores rutas para llegar a todos los destinos posibles
def dijkstra_entre_dos_nodos(G, inicio, fin):
    return nx.dijkstra_path(G, inicio, fin), nx.dijkstra_path_length(G, inicio, fin)

def mostrar_rutas_costos(rutas, costos):
    for destino, ruta in rutas.items():
        print(f"\nDesde {ruta[0]} hasta {destino} la ruta más barata es: {' -> '.join(ruta)}, con un costo de ${costos[destino]}")

# Cargar las rutas desde el archivo
G = cargar_rutas('rutas.txt')

# Solicitar al usuario la estación de salida
inicio = input("Por favor, ingresa el nombre de la estación de salida: ")

# Ejecutar el algoritmo de Dijkstra
rutas, costos = dijkstra(G, inicio)

# Mostrar las rutas y costos
mostrar_rutas_costos(rutas, costos)

# Dibujar el grafo
dibujar_grafo(G, inicio)