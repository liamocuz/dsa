"""
Implements a FIFO Queue data structure using a Doubly Linked List
"""
from typing import TypeVar
from linked_list import Node, DLL

T = TypeVar('T')

class Queue[T]:
    """
    The Queue class
    We places all new values at the back of the DLL and remove new values
    from the head of the DLL
    """
    def __init__(self) -> None:
        self.dll = DLL(None)

    def enqueue(self, val: T) -> None:
        """
        Add a value to the front of the queue
        """
        if self.dll.head:
            self.dll.add(Node(val))
        else:
            self.dll.head = Node(val)
            self.dll.tail = self.dll.head

    def dequeue(self) -> T:
        """
        Removes a value from the front of the queue
        """
        # If the queue is empty, return None
        if not self.dll.head:
            return None

        # Remove the head node and return it
        old_head: Node = self.dll.head
        if old_head.next:
            new_head: Node = old_head.next
            new_head.prev = None
            self.dll.head = new_head
        else:
            self.dll.head = None

        return old_head.val

if __name__ == "__main__":
    myqueue = Queue()

    myqueue.enqueue("Liam")
    myqueue.enqueue("Pat")
    myqueue.enqueue("Mike")
    myqueue.dll.print()
    print()

    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    myqueue.dll.print()
