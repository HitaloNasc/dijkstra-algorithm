def dijkstra(graph, start, end):
    """
    Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto entre dois nós de um grafo ponderado.

    Args:
        graph -- dicionário de dicionários representando o grafo ponderado, onde cada chave é um vértice e cada valor é outro dicionário contendo os vizinhos e os pesos das arestas.
        start -- vértice de partida para a busca do caminho mínimo.
        end -- vértice de chegada para a busca do caminho mínimo.

    Returns:
        Um dicionário contendo o caminho mínimo entre os vértices de partida e chegada. Se não houver um caminho válido, o dicionário estará vazio.
    """

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    path = {}

    while len(visited) < len(graph):
        current_vertex = None
        current_distance = float('inf')

        for vertex, distance in distances.items():
            if vertex not in visited and distance < current_distance:
                current_vertex = vertex
                current_distance = distance

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex

    path_list = []
    vertex = end
    while vertex != start:
        path_list.append(vertex)
        vertex = path[vertex]
    path_list.append(start)
    path_list.reverse()

    return distances[end], path_list
