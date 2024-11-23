#pylint: disable=all
"""
The idea behind merge sort is to continually split the array into subarrays, sort when they are small (<= 2),
and then merge them back together in order
Each iteration the middle of the array is found and then split into a left subarray and right subarray
This is done until there are two elements left in a subarary. They are ordered and then merged back together
with its opposite subarray.

QuickSort is usually preferred over Merge Sort as the constants of QuickSort are smaller.

Best Case: O(n log n) time | O(n) space
Average Case: O(n log n) time | O(n) space
Worst Case: O(n log n) time | O(n) space
"""

def mergeSort(arr: list[int], low: int, high: int) -> None:
    """
    Sorts the array arr in-place
    """
    # This is the recursive base case, when the array is of length 1
    if low >= high:
        return
    
    mid: int = low + (high - low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)

    merge(arr, low, mid, high)

    return

def merge(arr: list[int], low: int, mid: int, high: int):
    """
    Merge the sorted arrays back together and store in the original array
    The two arrays are defined by L and R
    """
    i = 0       # iterate through L
    j = 0       # iterate through R
    k = low     # iterate through the places in arr 

    # Take slices of the two already sorted arrays to be merged
    L = arr[low:mid + 1]        # left side of array
    R = arr[mid + 1:high + 1]   # right side of array

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return 

if __name__ == "__main__":
    arr1 = [123, 1, 5, 17, 10, 22, 44, 122, 10, 5]
    arr2 = [8, 5, 2, 9, 5, 6, 3]
    arr3 = [1, -1]

    print(arr1)
    mergeSort(arr1, 0, len(arr1) - 1)
    print(arr1)

    print(arr2)
    mergeSort(arr2, 0, len(arr2) - 1)
    print(arr2)

    print(arr3)
    mergeSort(arr3, 0, len(arr3) - 1)
    print(arr3)
