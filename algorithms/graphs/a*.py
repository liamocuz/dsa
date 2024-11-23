#pylint: disable=all

"""
The A* algorithm is a path finding algorithm used to find the shortest path between a start and end node.
It works by branching from the start to the end and considers it's next node to visit via a heuristic value.
In this example, the heuristic we used is the Manhattan Distance.
This algorithm works better than Dijkstras because of the bias the heuristic introduces, making it always search towards the end.

O(w * h * log(w * h)) time
O(w * h) space
"""

class Node:
    def __init__(self, row: int, col: int, value: int):
        self.id = str(row) + '-' + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.GScore = float("inf")  # distance from start
        self.FScore = float("inf")  # estimated distance to end
        self.previous = None        # node that this node came from

def sStar(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.GScore = 0
    startNode.FScore = getHeuristic(startNode, endNode)

    nodesToVisit = minHeap([startNode])
    while len(nodesToVisit.items) > 0:
        currentMinDistanceNode = nodesToVisit.poll()

        if currentMinDistanceNode == endNode:
            break
    
        neighbors = getNeighbors(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1: # is an obstacle
                continue

            tentativeDistanceToNeighbor = currentMinDistanceNode.GScore + 1
            if tentativeDistanceToNeighbor >= neighbor.GScore:
                continue
            neighbor.previous = currentMinDistanceNode
            neighbor.GScore = tentativeDistanceToNeighbor
            neighbor.FScore = tentativeDistanceToNeighbor + getHeuristic(neighbor, endNode)

            if not nodesToVisit.contains(neighbor):
                nodesToVisit.add(neighbor)
            else:
                nodesToVisit.update(neighbor)

    return reconstructPath(endNode)

"""
Calculates a Manhattan distance from a node to the end node
Manhattan Distance = abs(currentNode.row - endNode.row) + abs(currentNode.col - endNode.col)
"""
def getHeuristic(currentNode, endNode):
    return abs(currentNode.row - endNode.row) + abs(currentNode.col - endNode.col)

def getNeighbors(node, nodes):
    neighbors = []
    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col

    if row < numRows - 1:
        neighbors.append(nodes[row + 1][col])
    if row > 0:
        neighbors.append(nodes[row - 1][col])
    if col < numCols - 1:
        neighbors.append(nodes[row][col + 1])
    if col > 0:
        neighbors.append(nodes[row][col - 1])

    return neighbors

def reconstructPath(endNode):
    if not endNode.previous:
        return []
    
    path = []
    currentNode = endNode

    while currentNode:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.previous

    return path[::-1]


def initializeNodes(graph: list[list[int]]):
    nodes = []

    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))

    return nodes