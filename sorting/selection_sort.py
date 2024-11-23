#pylint: disable=all
"""
Selection Sort works by iterating through the array and selecting the smallest element in the unsorted sublist.
It then swaps the smallest element with the first element in the unsorted sublist.
The sorted sublist is then increased by one element and the unsorted sublist is decreased by one element.

Best Case: O(n^2) time | O(1) space
Average Case: O(n^2) time | O(1) space
Worst Case: O(n^2) time | O(1) space
"""

def selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts arr in place using selection sort
    """
    # Initial loop to go over all elements
    for i in range(len(arr)):
        smallest = i
        # Find smallest element in the unsorted sublist
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        # Swap new found smallest element with the next element in the sorted sublist
        arr[i], arr[smallest] = arr[smallest], arr[i]


if __name__ == "__main__":
    arr = [44, 13, 7, -11, -1210, 54, 22, 89]

    print(arr)
    selection_sort(arr)
    print(arr)
