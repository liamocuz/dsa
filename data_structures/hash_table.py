"""
Implements a very basic string hash table
It is implemented here with an array that can be indexed into and then
the array points to a linked list where the value lives
"""
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T')
TABLE_SIZE: int = 10

# These Node and SLL classes are the same from linked_list,
# but Node has both a key and a value as the key is needed
# for the hash table too
@dataclass
class Node[T]:
    """
    A pointer to hold a value and the next and previous pointers of
    following and previous Nodes
    """
    key: str
    val: T
    next: 'Node' = None
    prev: 'Node' = None

class SLL:
    """
    A Singularly Linked List where only the next pointer in the Node
    class is used and tracked
    """
    def __init__(self, head: Node):
        self.head: Node = head
        self.tail: Node = head

    def add(self, node: Node):
        """
        Adds a node to the end of the SLL 
        """
        # There are no nodes in the SLL
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print(self) -> None:
        """
        Prints the whole list from head to end
        """
        node: Node = self.head
        while node:
            print(f"Key={node.key}, Val={node.val}")
            node = node.next

class HashTable[str, T]:
    """
    The HashTable class that maps a string key to any value val
    """
    def __init__(self):
        self.table = [SLL(None) for _ in range(TABLE_SIZE)]

    def add(self, key: str, val: T) -> None:
        """
        Add a value into the hash table given the key
        """
        index: int = ascii_hash(key) % TABLE_SIZE
        self.table[index].add(Node(key, val))

    def __setitem__(self, key: str, val) -> None:
        self.add(key, val)

    def get(self, key: str) -> T:
        """
        Return a value from the hash table given the key
        """
        index: int = ascii_hash(key) % TABLE_SIZE
        node: Node = self.table[index].head
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def __getitem__(self, key: str) -> T:
        return self.get(key)

    def print(self):
        """
        Prints the hash table
        """
        for sll in self.table:
            sll.print()

def ascii_hash(string: str) -> int:
    """
    Hashes a string using a really bad hashing algorithm
    """
    hash_val: int = 0
    for i, ch in enumerate(string):
        hash_val += ord(ch) + i
    return hash_val

if __name__ == "__main__":
    my_table = HashTable()
    my_table.print()

    names = [("Liam", "Cuozzo"), ("Pat", "Limerick"), ("Mike", "Carlucci")]

    for name in names:
        my_table.add(*name)

    my_table.print()
    print()

    my_table["Finn"] = "Cuozzo"
    print(my_table["Finn"])
    my_table["nniF"] = "ozzuoC"
    print(my_table["nniF"])
