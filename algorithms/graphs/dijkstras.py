"""
An implementation of Dijkstra's Algorithm to find the Single-Source Shortest Path in a weighted
graph with non-negative weights
"""

from collections import deque


def dijkstras(start: int, edges: dict[int, list[tuple[int, int]]]) -> dict[int, list[int]]:
    """
    Find the single-source shortest path from the start vertex to all other vertices
    Dijkstra's algorithm cannot work on graphs with negative weight edges
    I only wrote this to work on undirected graphs
    Return a mapping of the vertex and its path to get to the start vertex

    Time: O(V^2) or O(E)
        If the graph is complete, then would need to visit every edge between all vertices
    Space: O(V)
        Need to store a table of length V
    """
    # Maintain a table that keeps track of distances to the start and through what vertex it
    # can reach the start
    table: dict[int, tuple[int, int]] = {i: (float("inf"), None) for i in edges.keys()}
    table[start] = (0, None)

    visited_vertices: set[int] = set()
    queue: deque = deque([start])

    while queue:
        current_vertex: int = queue.popleft()
        current_cost: int = table[current_vertex][0]
        for dst, cost in edges[current_vertex]:
            if current_cost + cost < table[dst][0]:
                table[dst] = (current_cost + cost, current_vertex)

            if dst not in visited_vertices:
                queue.append(dst)
        visited_vertices.add(current_vertex)

    return create_paths(start, table)


def create_paths(start: int, table: dict[int, tuple[int, int]]) -> dict[int, tuple[int, list[int]]]:
    """
    Returns a dictionary that maps the cost and path to get to another vertex from the start
    I don't think this function is correct
    """
    if not table:
        return {}

    result: dict[int, tuple[int, list[int]]] = {i: (0, []) for i in table.keys()}

    for src in table.keys():
        current_vertex: int = src
        path: list[int] = []
        while current_vertex != start:
            path.append(current_vertex)
            current_vertex = table[current_vertex][1]
        result[src] = (table[current_vertex][0], path[::-1])

    return result

if __name__ == "__main__":
    # An undirected weighted graph
    graph_edges: dict[int, list[tuple[int, int]]] = {
        0: [(1, 1), (3, 2), (2, 7)],
        1: [(0, 1), (4 ,4)],
        2: [(0, 7), (3, 3)],
        3: [(0, 2), (2, 3), (4, 5)],
        4: [(3, 5), (5, 3), (1, 4)],
        5: [(4, 3)]
    }

    print(dijkstras(0, graph_edges))
    print(dijkstras(2, graph_edges))
