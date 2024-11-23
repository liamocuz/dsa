#pylint: disable=all
"""
Taken from Leetcode 5
"""

def lps(s: str) -> str:
    # Idea: Loop through s, and at each point, expand outwards at each point
    #       Do the expansion twice, once for an odd len palindrome, and once for an even len palindrome
    #       Find the indices where the palindrome exists and keep track of the longest distance

    # Time: O(n^2)
        # Loop over array once, then expand twice for each char
    # Space: O(1)
        # No aux space

    if not s or len(s) == 1:
        return s

    longest_s: int = 0
    longest_e: int = 0
    for i in range(len(s) - 1):
        odd_s, odd_e = expand(s, i, i)
        even_s, even_e = expand(s, i, i + 1)

        if (odd_e - odd_s) > (longest_e - longest_s):
            longest_s = odd_s
            longest_e = odd_e
        if (even_e - even_s) > (longest_e - longest_s):
            longest_s = even_s 
            longest_e = even_e

    return s[longest_s: longest_e]


def expand(s: str, left: int, right: int) -> tuple[int, int]:
    """
    Returns the beginning and end indices of the found palindrome
    """

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    # Return [left+1, right) because we want to take a slice of s
    return (left + 1, right)


if __name__ == "__main__":
    
    print(lps("babad"))
    print(lps("cbbc"))
    print(lps("anchannahasdjcjbasdbhaaaaanaaaaahcc"))
