class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.conns: list[Node] = []

    def dfs_print(self):
        for node in self.conns:
            node.dfs_print()
            print(node.val)

    def bfs_print(self):
        for node in self.conns:
            print(node.val)
        for node in self.conns:
            node.bfs_print()

class DirectedGraph:
    def __init__(self, start: Node):
        self.start = start

def dfs(graph: DirectedGraph):
    for node in graph.start.conns:
        node.dfs_print()
        print(node.val)
    print(graph.start.val)

def bfs(graph: DirectedGraph):
    queue = [graph.start]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val)
        for child in current.conns:
            queue.append(child)


if __name__ == "__main__":
    mygraph = DirectedGraph(None)

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)
    node6 = Node(60)
    node7 = Node(70)

    mygraph.start = node1
    node1.conns.append(node2)
    node2.conns.append(node3)
    node1.conns.append(node4)
    node4.conns.append(node5)
    node4.conns.append(node6)
    node5.conns.append(node7)

    print("DFS")
    dfs(mygraph)
    print("BFS")
    bfs(mygraph)