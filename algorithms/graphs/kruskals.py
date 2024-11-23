"""
An implementation of Kruskal's Algorithm to create Minimum Spanning Trees
"""

import heapq
from disjoint_set import UnionFind

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

def kruskals(edges: dict[int, list[tuple[int, int]]]) -> list[Edge]:
    """
    Constructs a minimum spanning tree given the edges of a graph

    1. Sort all edges by their weights in ascending order
        - Sorting is done via a MinHeap
    2. Add edges in that order into the MST. Skip the edges that would create a cycle in the MST
        - Cycle checking is done via UnionFind
    3. Repeat step 2 until V-1 edges are added

    Time: O(E log E)
        Creates edges from the adjacency list in O(E) time
        Creates a heap in O(E) time
        UnionFind takes O(Eackermann(V)) time
        Pops E-1 edges from the heap which takes O(log E) time
        So O(E) + O(E) + O(E * ackermann(V)) + O(E) * O(log E)
    Space: O(E)
        Creates a set of edges
        Creates a UnionFind object which is O(E) space
    """
    # Create a list of unique edges
    # The given edges object has 2E entries in it because each src and dst is specified
    # going both ways
    edge_set: set[Edge] = set()
    for src, neighbors in edges.items():
        for dst, cost in neighbors:
            edge = Edge(src, dst, cost)
            if edge not in edge_set:
                edge_set.add(edge)

    # Create a min_heap from the edge_set
    min_heap: list = list(edge_set)
    heapq.heapify(min_heap)

    mst: list[Edge] = []
    total_vertices: int = len(edge_set) + 1

    # Create a UnionFind object to aid in the checking of cycles when adding
    # edges into the final MST
    uf: UnionFind = UnionFind(total_vertices)

    while min_heap and len(mst) < total_vertices - 1:
        edge: Edge = heapq.heappop(min_heap)

        # Make sure this adding this edge does not create a cycle
        if not uf.connected(edge.src, edge.dst):
            uf.union(edge.src, edge.dst)
            mst.append(edge)

    return mst

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

    minumum_spanning_tree: list = kruskals(graph_edges)
    print(minumum_spanning_tree)
