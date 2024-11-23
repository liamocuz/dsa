"""
An implementation of Prim's Algorithm to create Minimum Spanning Trees
"""

from collections import deque
import heapq

class Edge:
    """
    Represents an edge in a weighted undirected graph
    Overrides some methods to ensure uniqueness in a set
    This is useful because the edges are given as an adjacency list
    which would create 2E edges
    """
    def __init__(self, src: int, dst: int, cost: int) -> None:
        self.src = src
        self.dst = dst
        self.cost = cost

    def __lt__(self, other: 'Edge') -> bool:
        return self.cost < other.cost

    def __hash__(self) -> int:
        return hash((self.src, self.dst)) + hash((self.dst, self.src))

    def __eq__(self, other: 'Edge') -> bool:
        return hash(self) == hash(other)

    def __repr__(self) -> str:
        return f"(src:{self.src}, dst:{self.dst}, cost:{self.cost})"

def prims(edges: dict[int, list[tuple[int, int]]]) -> list[Edge]:
    """
    Constructs a minimum spanning tree given the edges of a graph

    1. Use two sets, one to track visited vertices and one to track un-visited vertices
        - Here we use an array instead
    2. Out of all edges that connect the vertices in the visited set with the vertices in the
    un-visited set, choose the edge with the smallest weight

    Time: O(V * log E)
        Loop over all vertices and then get the edges from the heap
    Space: O(V + E)
        Need to store V vertices and E edges
    """

    unvisited_vertices: list = list(edges.keys())
    num_vertices: int = len(edges)
    # Used to track the smallest edges that span the two sets
    min_heap: list = []
    mst: set = set()

    while unvisited_vertices and len(mst) < num_vertices - 1:
        vertex: int = unvisited_vertices.pop()

        # Now get all edges from visited_set to unvisited_set
        for dst, cost in edges[vertex]:
            new_edge: Edge = Edge(vertex, dst, cost)
            # Only want to add the edge if it is not already considered nor
            # if it was already added to the mst
            if new_edge not in mst:
                heapq.heappush(min_heap, new_edge)
        # Find the smallest edge in O(log E) time
        smallest_edge: Edge = heapq.heappop(min_heap)
        mst.add(smallest_edge)

    return list(mst)


if __name__ == "__main__":
    # edges is a dict that maps a source vertex to an adjacency
    # list of tuples where t[0] is the dest vertex, t[1] is the cost
    # This adjacency list ends up with 2E total edges in the data structure
    graph_edges: dict[int, list[tuple[int ,int]]] = {
        0: [(1, 1), (3, 2), (2, 7)],
        1: [(0, 1), (4 ,4)],
        2: [(0, 7), (3, 3)],
        3: [(0, 2), (2, 3), (4, 5)],
        4: [(3, 5), (5, 3), (1, 4)],
        5: [(4, 3)]
    }

    prim_mst: list = prims(graph_edges)
    print(prim_mst)
