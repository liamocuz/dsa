#pylint: disable=all

"""
Taken from Leetcode 33
"""

def search(nums: list[int], target: int) -> int:
    """
    
    """
    # Idea: The nums list is an ascending sorted order list that has been rotated by some value k
    #       We can perform a single binary search on the list because we know that when we find mind
    #       at least one side of the array must be in correct sorted order
    #       So at each point, find mid, find which side is in correct order, perform the normal
    #       binary search check, and adjust pointers accordingly   

    # Time: O(log n)
        # Perform a single binary search
    # Space: O(1)
        # No aux space

    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        mid: int = left + (right - left) // 2

        # Found the target index
        if nums[mid] == target:
            return mid

        # Left subarray is properly sorted
        elif nums[left] <= nums[mid]:
            # The target is in this left subarray
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            # The target must still be in the right subarray
            else:
                left = mid + 1


        # Right subarray is properly sorted
        elif nums[right] >= nums[mid]:
            # THe target is in this right subarray
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            # The target must still be in the left subarray
            else:
                right = mid - 1

    # Did not find the target
    return -1


if __name__ == "__main__":
    nums: list[int] = [4, 5, 6, 7, 0, 1, 2]
    
    print(search(nums, 0))
    print(search(nums, 3))
    print(search(nums, 5))