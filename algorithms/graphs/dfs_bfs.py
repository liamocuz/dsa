def dfs(graph, start):
    stack = []
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

def dfs_rec(graph, start):
    print(start)
    for neighbor in graph[start]:
        dfs_rec(graph, neighbor)

def bfs(graph, start):
    queue = []
    queue.append(start)

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


if __name__ == "__main__":

    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

    graph2 = {
        'A': ['B', 'D', 'E'],
        'B': ['C'],
        'C': [],
        'D': [],
        'E': ['F'],
        'F': ['G', 'H'],
        'G': [],
        'H': []
    }

    print("DFS")
    dfs(graph2, 'A') # acebdf
    print("\n")
    print("BFS")
    bfs(graph2, 'A') # abcdef
