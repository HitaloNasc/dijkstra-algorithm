import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk


def build(edges):
    """
    Constrói e retorna um grafo a partir de uma lista de arestas.

    Args:
        edges (list): Uma lista de com 2 itens representando as arestas do grafo.


    Returns:
        graph: Um dicionário de dicionários representando o grafo.

    """
    graph = {}
    for edge in edges:
        source = edge[0]
        dest = edge[1]
        weight = edge[2] if len(edge) == 3 else 1

        if source not in graph:
            graph[source] = {}
        if dest not in graph:
            graph[dest] = {}

        graph[source][dest] = weight
        graph[dest][source] = weight

    return graph


def show_route(graph, route):
    """
    Constrói e retorna um grafo no formato de gráfico apenas com os nós filhos dos nós na rota.

    Args:
        graph (dicionário): um grafo no formato de dicionário.
        route (list): uma lista de nós conectados.


    Returns:
        um gráfico mostrando a rota passada como parâmetro.
    """
    G = nx.Graph()

    for node in graph:
        if node in route:
            G.add_node(node)

    for source in graph:
        if source in route:
            for target, weight in graph[source].items():
                G.add_edge(source, target, weight=weight)

    pos = nx.spring_layout(G, k=0.25)
    nx.draw(G, pos, with_labels=True)
    path_edges = list(zip(route, route[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                           edge_color='r', width=3)
    plt.show()


def print_path_route(start, target, distance, route, window):
    """
    Imprime na interface gráfica o caminho passado como parâmetro.

    Args:
        start (string): um nó pertecente ao grafo.
        target (string): um nó pertecente ao grafo.
        distance (int): a distância entre os nós.
        route (list): uma lista de nós conectados.
        window (tk.Tk): interface gráfica


    Returns:
        um gráfico mostrando a rota passada como parâmetro.
    """
    label = tk.Label(
        window, text=f"Distância mínima de {start} até {target}: {distance}")
    label.pack()
    label = tk.Label(
        window, text=f"Seguindo o caminho:")
    label.pack()

    for index in range(len(route)):
        if route[index] != target:
            label = tk.Label(
                window, text=f"-> De {route[index]} para {route[index + 1]}")
            label.pack()
