"""
Implements the classic binary search algorithm in Python
Binary Search can only work on sorted arrays
This also includes arrays that have been rotated but are still in some sorted order

Time: O(log n)
    At each point discards checking half the array
Space: O(1)
    Runs in place
"""


def binary_search(arr: list[int], value: int) -> int:
    """
    The Binary Search method
    Operates on an array and looks for a value in that array
    Returns the index in where the value exists
    """
    low: int = 0
    high: int = len(arr) - 1

    while low <= high:
        mid: int = low + (high - low) // 2      # This is a trick mid calculation to avoid overflow

        if arr[mid] == value:
            return mid
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(binary_search(nums, 1))
