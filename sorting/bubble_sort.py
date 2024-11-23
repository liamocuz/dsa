#pylint: disable=all
"""
The idea behind bubble sort is to swap adjacent elements if they are out of order.
The largest element will "bubble up" to the end of the array after each iteration.

Best Case: O(n) time | O(1) space
Average Case: O(n^2) time | O(1) space
Worst Case: O(n^2) time | O(1) space
"""

def bubble_sort(array: list[int]) -> None:
    """
    Sorts the array arr in-place using bubble sort.
    """
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    arr = [10, 2, 15, 11, -6, 1502, 3]

    print(arr)
    bubble_sort(arr)
    print(arr)
