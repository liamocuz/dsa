#pylint: disable=all
"""
The quickselect algorithm used to find the kth smallest/largest element in an unordered list.

It is very similar to quick_sort but instead of sorting both sides of the partition,
it only sorts the side that contains the kth smallest element.

This works because of the partition property that splits the list into two parts,
where each half is sorted relative to the pivot.

Best Case: O(n) time | O(log n) space
Average Case: O(n) time | O(log n) space
Worst Case: O(n^2) time | O(log n) space
"""

def quick_select_smallest(arr: list[int], left: int, right: int, k: int) -> int:
    """
    The quickselect algorithm used to find the kth smallest element in an unordered list.
    """

    if left == right:
        return arr[left]

    pivot: int = partition(arr, left, right)
    # If the pivot return is larger then k - 1,
    # we need to check to the left of the pivot for k
    if pivot > k - 1:
        return quick_select_smallest(arr, left, pivot - 1, k)
    # If the pivot returned is less than k - 1,
    # we need to check to the right of the pivot for k
    elif pivot < k - 1:
        return quick_select_smallest(arr, pivot + 1, right, k)
    # Otherwise we found exactly at k and can return arr[pivot] which is k
    # as pivot is in the kth sorted position in the array
    else:
        return arr[pivot]

def quick_select_largest(arr: list[int], left: int, right: int, k: int) -> int:
    """
    The quickselect algorithm used to find the kth largest element in an unordered list.
    """
    if left == right:
        return arr[left]

    pivot: int = partition(arr, left, right)
    if pivot > len(arr) - k:
        return quick_select_largest(arr, left, pivot - 1, k)
    elif pivot < len(arr) - k:
        return quick_select_largest(arr, pivot + 1, right, k)
    else:
        return arr[pivot]


def partition(arr: list[int], left: int, right: int) -> int:
    """
    Quick Sort partition with Hoare's algorithm, using the right-most element as the pivot
    """
    pivot: int = right
    pivot_val: int = arr[pivot]

    # We move i and j immediately in the loop, so start one off
    # j is already one off since we choose right as the pivot
    i: int = left - 1
    j: int = right

    while True:
        # Look for a value larger than the pivot_val in the left side of the array
        i += 1
        while arr[i] < pivot_val:
            i += 1
        
        # Look for a value less than the pivot_val in the right side of the array
        j -= 1
        while arr[j] > pivot_val:
            if j == left:
                break
            j -= 1

        # If the pointers have crossed, then the pivot is in its sorted position
        if i >= j:
            break
        # Swap the two values to be on the correct sides of the pivot
        swap(arr, i, j)

    # Swap the pivot into its correct sorted position
    # We swap with i since it is larger that the pivot val
    swap(arr, i, pivot)
    return i

def swap(arr: list[int], idx1: int, idx2: int) -> None:
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


if __name__ == "__main__":
    # Sorted: 2, 3, 5, 6, 7, 8, 9
    # 3rd smallest is 5
    arr = [8, 5, 2, 9, 7, 6, 3]

    print(arr)
    print(sorted(arr))
    kth_smallest: int = quick_select_smallest(arr[:], 0, len(arr) - 1, 3)
    print(kth_smallest)

    kth_largest: int = quick_select_largest(arr[:], 0, len(arr) - 1, 3)
    print(kth_largest)

