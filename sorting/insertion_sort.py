#pylint: disable=all
"""
Insertion Sort works by iterating through the array and inserting the current element into its correct position.
It maintains a sorted sublist in the lower indices of the array and an unsorted sublist in the higher indices.

Best Case: O(n) time | O(1) space
Average Case: O(n^2) time | O(1) space
Worst Case: O(n^2) time | O(1) space
"""
def insertion_sort(arr: list[int]) -> None:
    """
    Sort arr in place using insertion sort.
    """

    # Treat the first element as the sorted sublist
    for i in range(1, len(arr)):
        j = i
        # Insert the current element into the sorted sublist
        # Similar to bubble sort, but you bubble down into the sorted sublist
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return

if __name__ == "__main__":
    arr = [52, 11, -9, 121, 45, -90, 44]

    print(arr)
    insertion_sort(arr)
    print(arr)
