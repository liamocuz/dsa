#pylint: disable=all
"""
The idea behind quickSort is to find the sorted position of one element at a time in the array
An element is sorted if all elements to its left are less than and all elements to the right are greater
The pivot position is chosen to be the lowest index in the subarray that is being worked on
While the two pointers i and j are finding a value less than the pivot and greater than or equal to respectively
Swap the values in those positions. When i is finally larger than j, swap the value at j and the pivot
The pivot is now in its sorted position.
Next do the same algorithm but change the low and high indices to be the two subarrays on either side of the last pivot position

Some suggestions to improve partitioning
1. Select random element as pivot
2. Select median of first, middle and last element as pivot

Best Case: O(n log n) time | O(log n) space
Average Case: O(n log n) time | O(log n) space
Worst Case: O(n^2) time | O(log n) space

The O(n log n) time complexity is derived by the fact that we iterate over the whole array at each partition step
and then divide the array into two subarrays. This is done log n times because the array is divided in half each time.
"""

def improved_quick_sort(arr: list[int], left: int, right: int) -> None:
    """
    A few ways to improve Quick Sort include:
        1. Choosing from a median of three chosen values
        2. Cutting off to insertion sort, as insertion sort is faster at smaller partition sizes
        3. Partition the array into three parts, one for items with smaller keys,
           one for items with larger keys, and one for items with equal keys
    """
    if left >= right:
        return

    # Find the mid element
    mid: int = left + (right - left) // 2
    # Find the median of the three choices
    pivot: int = sorted([left, mid, right], key=lambda x: arr[x])[1]
    # We swap because we want the pivot to be placed at the right, which is where the partition will grab it
    # and compare with the other values in the array
    swap(arr, pivot, right)

    pivot: int = hoare_partition(arr, left, right)
    improved_quick_sort(arr, left, pivot - 1)
    improved_quick_sort(arr, pivot + 1, right)

    return

def pythonic_quick_sort(arr: list[int]) -> list[int]:
    """
    This implementation is very pythonic in the array slices.
    It uses point 3 from the improvied_quick_sort where it does the three way partitioning.
    It is not in-place so therefore uses more memory.
    It splits the array into three arrays: less, equal, and greater.
    It then runs recursively on less and greater and creates an array by adding the arrays together.
    """
    if len(arr) <= 1:
        return arr

    # Choose the middle element as the pivot
    pivot: int = len(arr) // 2
    pivot_val: int = arr[pivot]

    less: list[int] = [x for x in arr if x < pivot_val]
    equal: list[int] = [x for x in arr if x == pivot_val]
    greater: list[int] = [x for x in arr if x > pivot_val]
    return pythonic_quick_sort(less) + equal + pythonic_quick_sort(greater)

# O(log n) operations
def base_quick_sort(arr: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    pivot: int = hoare_partition(arr, left, right)
    base_quick_sort(arr, left, pivot - 1)
    base_quick_sort(arr, pivot + 1, right)

    return

def hoare_partition(arr: list[int], left: int, right: int) -> int:
    """
    Quick Sort partition with Hoare's algorithm, using the right-most element as the pivot
    """
    # Choose the right-most element as the pivot 
    pivot: int = right 
    pivot_val: int = arr[pivot]

    # Two variables to scan from each side
    # We initialize i to be one off because the first thing it does is increment
    # We initialize j to be one off because the first thing it does is decrement
    i = left - 1
    j = right

    # Hoare partition from Sedgewick
    while True:
        # Find a value greater than or equal to the pivot to the left of the pivot
        i += 1
        while arr[i] < pivot_val:
            i += 1

        # Find a value less than or equal to the pivot to the right of the pivot
        j -= 1
        while arr[j] > pivot_val:
            # When the value you need to switch with is all the way to the left
            if j == left:
                break
            j -= 1

        # If the pointers have crossed, then the pivot is in its final position
        if i >= j:
            break
        swap(arr, i, j)

    # Swap chosen pivot into its final place
    # We do the swap with i since it is larger than the pivot
    swap(arr, i, pivot)
    return i

def left_hoare_partition(arr: list[int], left: int, right: int) -> int:
    """
    Quick Sort partition with Hoare's algorithm, using the left-most element as the pivot
    """
    # Choose the left-most element as the pivot 
    pivot: int = left 
    pivot_val: int = arr[pivot]

    # Two variables to scan from each side
    # They are initialized one off as the first thing they do is increment or decrement
    i = left
    j = right + 1

    # Hoare partition from Sedgewick
    while True:
        # Find a value greater than or equal to the pivot to the left of the pivot
        i += 1
        while arr[i] < pivot_val:
            # When the value you need to switch with is all the way to the right
            if i == right:
                break
            i += 1

        # Find a value less than or equal to the pivot to the right of the pivot
        j -= 1
        while arr[j] > pivot_val:
            j -= 1

        # If the pointers have crossed, then the pivot is in its final position
        if i >= j:
            break
        swap(arr, i, j)

    # Swap chosen pivot into its final place
    swap(arr, j, pivot)
    return j

def middle_hoare_partition(arr: list[int], left: int, right: int) -> int:
    """
    Just ignore this one pretty much and use the ones where you use the ends as the pivots
    I don't like this one since it doesn't place the chosen pivot in the middle afterwards,
    and therefore makes quick sort much harder to understand. This is because the pivot
    may be moved during the swaps.
    One thing that could be changed to fix this is swap the middle element with the right,
    and then just do the regular right Hoare partition.

    Quick Sort partition with Hoare's algorithm, using the middle element as the pivot
    A big difference with middle element is that there is no swapping of the chosen pivot into its final place
    The value return is indeed a valid pivot meaning it has the partition property
    So therefore at each call, we must also operate on the pivot itself
    """
    # Choose the right-most element as the pivot 
    pivot: int = left + (right - left) // 2
    pivot_val: int = arr[pivot]

    # Two variables to scan from each side
    i: int = left
    j: int = right

    while True:
        # Find a value greater than or equal to the pivot to the left of the pivot
        while arr[i] < pivot_val:
            i += 1

        # Find a value less than or equal to the pivot to the right of the pivot
        while arr[j] > pivot_val:
            j -= 1

        # If the pointers have crossed, then the pivot is in its final position
        if i >= j:
            break
        swap(arr, i, j)
        # The pointers need to be moved an extra element because when the next loop starts we
        # dont want to compare the same elements again. We want to move ahead.
        # This is different than left and right because since we use the ends as the pivots there,
        # it was nice to start one off because the first thing they do is increment or decrement.
        # Here since we are using the middle element as a pivot, we can just instead start from
        # the ends each time. But we need these extra increments and decrements to make sure we
        # move ahead.
        i += 1
        j -= 1

    return i

def right_lomuto_partition(arr: list[int], left: int, right: int) -> int:
    """
    Quick Sort partition with Lomuto's algorithm
    I don't like this algorithm as much because the scanning from left and right
    makes more sense to me. This is just simply scanning from a single side.
    """
    # Choose the right-most element as the pivot 
    pivot: int = right 
    pivot_val: int = arr[pivot]

    # The pointer to the last element that is less than the pivot
    i = left - 1

    # Lomuto partition from 
    for j in range(left, right):
        if arr[j] < pivot_val:
            i += 1
            swap(arr, i, j)

    # Swap chosen pivot into its final place
    swap(arr, i + 1, pivot)
    return i + 1

def swap(arr: list[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr1 = [10, 2, 15, 6, 122, 10, 44, 11]
    arr2 = [-421, 12, -12342, 10, 10, 55, 231, 102, 982, -10092, 3]
    arr3 = [8, 5, 2, 2, 9, 5, 6, 3]

    # Improved quick sort
    print(arr1)
    improved_quick_sort(arr1, 0, len(arr1) - 1)
    print(arr1)

    print(arr2)
    improved_quick_sort(arr2, 0, len(arr2) - 1)
    print(arr2)

    print(arr3)
    improved_quick_sort(arr3, 0, len(arr3) - 1)
    print(arr3)
    
    # Pythonic quick sort
    # print(arr1)
    # parr1 = pythonic_quick_sort(arr1)
    # print(parr1)

    # print(arr2)
    # parr2 = pythonic_quick_sort(arr2)
    # print(parr2)

    # print(arr3)
    # parr3 = pythonic_quick_sort(arr3)
    # print(parr3)
