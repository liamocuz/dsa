"""
This is a famous algorithm that tries to maximize the amount of value that can be carried in a knapsack with a capacity limit.
This can be solved using a matrix with the items on the y axis and all weights from 0 to weight in the x axis.
# of columns is capacity + 1, # of rows in items + 1.

O(nc) time
O(nc) space
n - number of items
c - capacity
"""
def knapsack(items: list[list[int]], capacity: int):
    knapsackValues = [[0 for _ in range(0, capacity + 1)] for _ in range(0, len(items) + 1)]

    for i in range(1, len(items) + 1):
        weight = items[i - 1][1]
        value = items[i - 1][0]
        for c in range(0, capacity + 1):
            if weight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - weight] + value)
    return  [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues: list[list[int]], items: list[list[int]]) -> list:
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1

    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    
    return list(reversed(sequence))


if __name__ == "__main__":
    items = [
        [1, 2],
        [4, 3],
        [5, 6],
        [6, 7]
    ]
    weight = 10

    print(knapsack(items, weight))