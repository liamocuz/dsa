#pylint: disable=all

"""
Dutch National Flag algorithm by Edsger Dijkstra

Sorts an array of 0, 1, or 2 in-place and with a single pass

Time: O(n) - Loops through once
Space: O(1) - In-place
"""

def dnf(nums: list[int]) -> None:
    """
    Dutch National Flag sort
    """
    # Idea: Use three pointers
    #       1. To track the right most 0 on the left of the array
    #       2. To track the left most 2 on the right of the array
    #       3. A curr pointer to travel through the array

    # Time: O(n)
        # Single traversal
    # Space: O(1)
        # In-Place

    if not nums:
        return
    
    p0: int = 0                 # 0 pointer
    p2: int = len(nums) - 1     # 2 pointer
    curr: int = 0               # loop through array

    while curr <= p2:
        # Swap curr into the next 0 spot
        # We are fine to increment both here because at any point,
        # the previous values behind curr have already been scanned
        if nums[curr] == 0:
            swap(nums, curr, p0)
            p0 += 1
            curr += 1
        # Swap curr into the next 2 spot
        elif nums[curr] == 2:
            swap(nums, curr, p2)
            p2 -= 1
            # We don't increment here because we just swapped a 
            # value into curr but haven't scanned it yet
        # A 1 so move along
        else:
            curr += 1

    return


def swap(nums: list[int], idx1: int, idx2: int) -> None:
    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]


if __name__ == "__main__":
    arr = [1, 2, 0, 0, 2, 2, 2, 0, 0, 1, 1, 1, 2, 0, 1]
    print(arr)
    dnf(arr)
    print(arr)

    arr2 = [2,0,2,1,1,0]
    print(arr2)
    dnf(arr2)
    print(arr2)
