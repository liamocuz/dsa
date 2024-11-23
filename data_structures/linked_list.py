"""
Implements a Singly Linked List and a Doubly Linked List.
A linked list is a series of linearly connected pointers that hold values.
"""
from dataclasses import dataclass

@dataclass
class Node[T]:
    """
    A pointer to hold a value and the next and previous pointers of
    following and previous Nodes.
    """
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
        self.tail.next = node
        self.tail = node

    def print(self):
        """
        Prints the whole list from head to end
        """
        node = self.head
        while node:
            print(node.val)
            node = node.next

class DLL:
    """
    A Doubly Linked List where each Node tracks its next and prev Nodes
    """
    def __init__(self, head: Node) -> None:
        self.head = head    # The first node in the list
        self.tail = head    # The last node in the list

    def add(self, node: Node) -> None:
        """
        Adds a node to the end of the DLL
        """
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    @staticmethod
    def add_after(node: Node, new_node: Node) -> None:
        """
        Adds a new_node after another node in the DLL
        """
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node

    @staticmethod
    def add_before(node: Node, new_node: Node) -> None:
        """
        Adds a new_node before another node in the DLL
        """
        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node

    def print(self) -> None:
        """
        Prints the whole list from head to end
        """
        node: Node = self.head
        while node:
            print(node.val)
            node = node.next

    def print_there_and_back(self) -> None:
        """
        Prints the whole list from head to end
        and then from end to head
        """
        node = self.head
        while node:
            print(node.val)
            node = node.next
        node = self.tail
        while node:
            print(node.val)
            node = node.prev


if __name__ == "__main__":
    sll = SLL(Node(10))
    sll.add(Node(20))
    sll.add(Node(30))
    # 10 -> 20 -> 30
    sll.print()
    print()

    dll = DLL(Node(100))
    dll.add(Node(200))
    dll.add(Node(300))
    # 100 <-> 200 <-> 300
    dll.print()
