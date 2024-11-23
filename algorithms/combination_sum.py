#pylint: disable=all

"""
Taken from Leetcode 39
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Given a list of candidates and a target, find all combinations of candidates that add up to target.
    Each candidate can be used an infinite amount of times.
    """

    # Idea: Perform a DFS traversal with backtracking
    #       At each level, decrement the number you go down the tree with
    #       If at that next leve, the number is 0, then you've found a valid combination
    #       If its negative, then you can't continue so return
    #       Otherwise, loop through the rest of the values in the candidates list from that point
    #       By only looping through the remainder of the list, we avoid duplicates

    # Time: O(n^((t/m) + 1))
        # This is a doozy
        # t is the target, m is the smallest value in the candidates
    # Space: O(t/m)
        # Implement with recursion that can add up to t/m
        # Also keep a combination of numbers of at most length t/m

    results: list[list[int]] = []

    def backtrack(remaining: int, current_combination: list[int], candidate_idx: int) -> None:
        # We have found a valid combination
        if remaining == 0:
            results.append(list(current_combination))
            return

        # Unable to proceed further
        elif remaining < 0:
            return

        for i in range(candidate_idx, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(remaining - candidates[i], current_combination, i)
            current_combination.pop()

        return

    backtrack(target, [], 0)
    return results


if __name__ == "__main__":
    candidates: list[int] = [2, 3, 6, 7]

    print(combination_sum(candidates, 7))

    candidates: list[int] = [2, 3, 5]
    print(combination_sum(candidates, 8))
