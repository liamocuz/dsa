"""
A Trie is a tree-like structure useful for matching if a subtring exists in another string
Here this trie matches the whole word, but other tries such as a prefix or suffix Trie can be used

Creation (adding a string):
O(n) time | O(n) space

Searching:
O(n) time | O(1) space
"""

MARKER: str = "*"

class Trie:
    """
    Creates a Trie class
    """
    def __init__(self) -> None:
        self.root = {}

    def insert(self, add_string: str) -> None:
        """
        Add the string into the Trie
        """
        level = self.root
        for char in add_string:
            if char not in level:
                level[char] = {}
            level = level[char]

        level[MARKER] = add_string

    def contains(self, search_string: str) -> bool:
        """
        Returns a boolean if the string exists in the trie
        """
        level = self.root
        for char in search_string:
            if char not in level:
                return False
            level = level[char]

        return MARKER in level

if __name__ == "__main__":
    big_string: str = "this is a big string"
    small_strings: list[str] = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
    result: list[bool] = []

    trie = Trie()

    tokens = big_string.split(" ")
    for token in tokens:
        trie.insert(token)

    for string in small_strings:
        result.append(trie.contains(string))

    print(result)
    assert(result == [True, False, True, True, False, True, False])
