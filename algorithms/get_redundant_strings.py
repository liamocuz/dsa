"""
This is the solution to an AWS SWE test that I took
I couldn't figure it out the first time, so here I practice it and save it
"""

def get_redunant_strings(word: str, a: int, b: int) -> int:
    """
    This function returns the amount of substrings in word that are redundant
    A string is redundant if len(string) == a * V + b * C
    Where V and C are the number of Vowels and Consonants in string
    word is a string only containig lowercase english letters
    """
    # Idea: Use a prefixSum approach to find the redundant substrings
    #       Loop through the string and keep track of the number of vowels
    #       and consonants at each point
    #       If len(subString) == a * V + b * C then we've found a redunant string
    #       But instead we do this lookup by finding a difference to remove from
    #       the front of the subString to get the difference to 0
    #       difference = a * V + b * C - (i + 1) where i + 1 is the length
    #       If that difference is in the map, then we know there is a subString to
    #       remove from the front. Remove however many subStrings match that difference
    #       in the map which means there are that many redunant subStrings up until that point

    if not word:
        return 0

    num_vowels: int = 0
    num_cons: int = 0

    num_redundant: int = 0

    # Maps the difference to the number of times it has already ocurred in the string
    # It always starts with 0: 1 because we know that to remove 0 chars from the string
    # is always possible
    differences: dict[int, int] = {0: 1}

    for i, ch in enumerate(word):
        if is_vowel(ch):
            num_vowels += 1
        else:
            num_cons += 1

        # Calculate the current difference of the current subString at i
        # i - 1 is equal to len(current_word)
        difference: int = a * num_vowels + b * num_cons - (i - 1)

        if difference in differences:
            # Add the number of prefix strings to remove to the num_redundant
            num_redundant += differences[difference]
            # Add this current subString to the difference
            differences[difference] += 1
        else:
            # Add this difference to the map if not seen before
            differences[difference] = 1

    return num_redundant


def is_vowel(ch: str) -> bool:
    """
    Returns if the char is a vowel or not
    """
    vowels: set = set(["a", "e", "i", "o", "u"])
    if ch in vowels:
        return True
    return False

if __name__ == "__main__":

    print(get_redunant_strings("abbacc", -1, 2))
    print(get_redunant_strings("akljfs", -2, 1))
