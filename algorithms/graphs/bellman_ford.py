"""
An implementation of the Bellman-Ford Algorithm to find the Single-Source Shortest Path in a
weighted graph with negative or positive weights
"""

from collections import deque

def bellman_ford(start: int, graph: dict[int, list[tuple[int, int]]]) -> dict[int, int]:
    """
    Find the single-source shortest path from a start vertex to all other vertices
    The Bellman-Ford algorithm cannot work with graphs with negative weight cycles

    Returns the cost to all other vertices from start

    Time: O(VE)
        Need to loop over all edges for all vertices in a complete graph
    Space: O(V)
        Store a table of V vertex distances
    """

    # Bellman-Ford requires that the shortest path be found with at most V-1 edges
    max_edges: int = len(graph) - 1

    previous: list[int] = [float("inf") for _ in range(len(graph))]
    previous[start] = 0
    current: list[int] = [float("inf") for _ in range(len(graph))]
    current[start] = 0

    # Relax the edges V - 1 times
    for _ in range(max_edges):
        # Loop over all edges
        for src in graph:
            for dst, cost in graph[src]:
                # If the previous is inifnity, then adding anything to it won't change
                if previous[src] == float("inf"):
                    continue

                # If previous and the new cost is less than the current, update the current
                if previous[src] + cost < current[dst]:
                    current[dst] = previous[src] + cost

        # We can break early if no changes were made when relaxing
        if current == previous:
            break

        # Make previous the current for the next iteration of relaxation
        previous = current.copy()

    # Check graph one more time for negative weight cycle detection
    # Theorem: If we relax V times and end up with a shorter distance, there must be
    # a negative weight cycle
    for src in graph:
        for dst, cost in graph[src]:
            if previous[src] != float("inf") and current[src] + cost < previous[dst]:
                raise ValueError("The graph contains a negative weight cycle")

    return {i: current[i] for i in range(len(current))}

def spfa(start: int, graph: dict[int, list[tuple[int, int]]]) -> dict[int, int]:
    """
    The Shortest Path Faster Algorithm
    Similar to Bellman-Ford, but uses just a simple queue and table instead
    Anytime a vertex distance is updated, that node is added to the queue to be
    evaluated again since it is likely its neighbors can be updated too
    Does not use the V - 1 theorem really
    
    Time: O(V * E)
        Loop over all edges for every vertex
    Space: O(V)
        Store V vertices
    """

    table: list[int] = [float("inf") for _ in range(len(graph))]
    table[start] = 0
    queue: deque = deque([start])

    while queue:
        src: int = queue.popleft()

        for dst, cost in graph[src]:
            if table[src] + cost < table[dst]:
                table[dst] = table[src] + cost
                queue.append(dst)

    return {i: table[i] for i in range(len(graph))}


if __name__ == "__main__":
    # A direct weighted graph
    graph_edges: dict[int, list[tuple[int, int]]] = {
        0: [(2, 500), (3, 200), (1, 100)],
        1: [(2, 100)],
        2: [(3, 100)],
        3: [(1, -150)]
    }

    print(bellman_ford(0, graph_edges))
    print(spfa(0, graph_edges))
