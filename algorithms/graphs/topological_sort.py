"""
Topological sort using Kahn's Algorithm
"""

import collections


def topological_sort(num_vertices: int, prerequisites: list[tuple[int, int]]) -> list[int]:
    """
    Creates a topological sorting of graph given the prerequisites of each vertex
    prerequisites are structured like (to, from), meaning you must process from before
    processing to

    Time: O(V + E)
    Process all vertices and then for each one processed, process all edges via adjacency list

    Space: O(V + E)
    Adjacency list and indegree dicts
    """

    # Create an adjacency list and an indegree mapping
    adjacency: dict[int, list[int]] = {i: [] for i in range(num_vertices)}
    indegree: dict[int, int] = {}

    for dest, src in prerequisites:
        if src not in adjacency:
            adjacency[src] = []
        adjacency[src].append(dest)

        if dest not in indegree:
            indegree[dest] = 0
        indegree[dest] += 1

    # Create a queue to load in the nodes with indegree 0
    # Loads in the vertex values that have an indegree of 0 so we can start the queue
    queue = collections.deque([i for i in range(num_vertices) if i not in indegree])

    result: list[int] = []

    while queue:
        vertex: int = queue.popleft()

        result.append(vertex)

        # Loop over vertices that are pointed to from vertex and
        # decrement their indegrees as we have now processed vertex
        for dependent in adjacency[vertex]:
            indegree[dependent] -= 1
            # If the indegree is now 0, we can add to the queue
            if indegree[dependent] == 0:
                queue.append(dependent)

    # If there is a cycle in the graph, we will be missing vertices in our output
    # So this is a final cycle detection
    return result if len(result) == num_vertices else []


if __name__ == "__main__":

    valid_prereqs = [
        # To take 1, take 0
        [1, 0],
        [2, 0],
        [3, 1],
        [1, 2],
        [3, 2]
    ]

    order: list = topological_sort(4, valid_prereqs)
    print(order)

    # Contain a cycle
    invalid_prereqs = [
        [1, 0],
        [2, 1],
        [3, 1],
        [0, 2],
        [3, 2]
    ]
    order: list = topological_sort(4, invalid_prereqs)
    print(order)
