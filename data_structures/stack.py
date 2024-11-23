"""
Implements a LIFO Stack data structure using a Singly Linked List
"""
from typing import TypeVar
from linked_list import Node, SLL

T = TypeVar('T')

class Stack[T]:
    """
    The Stack class
    All values are added and removed from the head of the queue
    """
    def __init__(self):
        self.sll = SLL(None)

    def push(self, val: T) -> None:
        """
        Add a value to the top of the stack
        """
        if self.sll.head:
            new_head: Node = Node(val)
            new_head.next = self.sll.head
            self.sll.head = new_head
        else:
            self.sll.head = Node(val)
            self.sll.tail = self.sll.head

    def pop(self) -> T:
        """
        Removes a value from the top of the stack
        If the stack is empty it returns None
        """
        if not self.sll.head:
            return None
        old_head: Node = self.sll.head
        new_head: Node = self.sll.head.next
        self.sll.head = new_head

        return old_head.val

if __name__ == "__main__":
    mystack = Stack()

    mystack.push("Liam")
    mystack.push("Pat")
    mystack.push("Mike")

    print(mystack.pop())    # Mike
    print(mystack.pop())    # Pat
    print(mystack.pop())    # Liam
    print(mystack.pop())    # None
