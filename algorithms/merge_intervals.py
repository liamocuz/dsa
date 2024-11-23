#pylint: disable=all

"""
From Leetcode 56
"""

def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Idea: Sort the intervals based on their start value
    #       Start with the first interval and loop through the rest
    #       If the intervals can be merged, merge them into the first
    #       Otherwise, append the current interval to the results 
    #       and make the current i interval the current interval

    # Time: O(n + nlogn) -> O(nlogn)
        # Sort and loop over once
    # Space: O(n + logn) -> O(nlogn)
        # Sort takes logn (quicksort depth) and storing results

    if not intervals:
        return intervals

    # Sort the intervals by the start value
    intervals.sort(key=lambda x: x[0])

    results: list[tuple[int, int]] = []

    current: tuple[int, int] = intervals[0]

    for i in range(1, len(intervals)):
        c_s, c_e = current
        i_s, i_e = intervals[i]

        # The intervals overlap
        if c_e >= i_s:
            current[0] = min(c_s, i_s)
            current[1] = max(c_e, i_e)
        # No overlap
        else:
            results.append(current)
            current = intervals[i]
            
    # Will have one leftover
    results.append(current)
    return results
    
if __name__ == "__main__":
    intervals = [[5, 6], [2, 4], [12, 15], [1, 3]]

    print(merge(intervals))
