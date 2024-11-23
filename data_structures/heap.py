#pylint: disable=missing-function-docstring, line-too-long
"""
Implements a Min and a Max heap in python
"""
from abc import ABC, abstractmethod
import heapq


class Heap(ABC):
    """
    An abstract class that MinHeap and MaxHeap can inherit from
    Both heaps have similar structure and methods, but different
    implementations of when they sift a value up or down when add() or
    pop() is called due to the comparisons needed.
    """

    def __init__(self) -> None:
        self.items: list = []

    def __len__(self) -> int:
        return len(self.items)

    def add(self, item: int) -> None:
        """
        When adding a value to a heap, the new item is placed at
        the end of the heap and then sifted up into its correct place
        """
        self.items.append(item)
        self.sift_up()

    def pop(self) -> int:
        """
        When popping a value from a heap, the root node is swapped with
        the last element in the heap, the final element is removed,
        and then the new root is sifted down into its correct place
        """
        if len(self.items) == 0:
            raise ValueError("Cannot pop from empty heap")
        root_val: int = self.peek()

        # Swap the last element into the root position
        self.items[0] = self.items[-1]
        # Remove the last element
        self.items.pop()
        # Sift the new root down into its correct place
        self.sift_down()

        return root_val

    def peek(self) -> int:
        """
        Get the top value of the heap
        """
        return self.items[0]

    @abstractmethod
    def sift_up(self) -> None:
        """
        Used when add() is called
        """

    @abstractmethod
    def sift_down(self) -> None:
        """
        Used when pop() is called
        """

    # Util Method
    def swap(self, index1: int, index2: int) -> None:
        """
        Swaps two values in an array
        """
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    # Get indices
    def get_left_child_index(self, parent_index: int) -> int:
        return (2 * parent_index) + 1
    def get_right_child_index(self, parent_index: int) -> int:
        return (2 * parent_index) + 2
    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    # Checks for children and parent existence
    def has_left_child(self, parent_index: int) -> bool:
        return self.get_left_child_index(parent_index) < len(self.items)
    def has_right_child(self, parent_index: int) -> bool:
        return self.get_right_child_index(parent_index) < len(self.items)
    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0

    # Get values
    def get_left_child(self, parent_index: int) -> int:
        if self.has_left_child(parent_index):
            return self.items[self.get_left_child_index(parent_index)]
        raise ValueError("No Left Child")

    def get_right_child(self, parent_index: int) -> int:
        if self.has_right_child(parent_index):
            return self.items[self.get_right_child_index(parent_index)]
        raise ValueError("No Right Child")

    def get_parent(self, index: int) -> int:
        if self.has_parent(index):
            return self.items[self.get_parent_index(index)]
        raise ValueError("No Parent")


class MinHeap(Heap):
    """
    Implementation of a MinHeap
    """

    def sift_up(self) -> None:
        """
        When a MinHeap needs to sift_up after add(),
        1. Start from last element
        1. Swap node with parent while the parent is larger than the node
        """
        # Start with last element
        index: int = len(self.items) - 1
        while self.has_parent(index) and self.get_parent(index) > self.items[index]:
            parent_index: int = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def sift_down(self) -> None:
        """
        When a MinHeap needs to sift_down after pop(),
        1. Start from root node
        2. Swap node with the smallest child while the node is larger than both children
        """
        # Start with root element
        index: int = 0

        # We make this the loop as if it no longer has a left child,
        # it will be a leaf node since a heap must be a complete binary tree
        while self.has_left_child(index):

            # Get the index of the smallest child
            smaller_index: int = self.get_left_child_index(index)
            if self.has_right_child(index) and (self.get_right_child(index) < self.get_left_child(index)):
                smaller_index = self.get_right_child_index(index)

            # If the current item is smaller than the smallest of its children
            # then we have restored the heap property and the node is in its corerct
            # place in the heap
            if self.items[index] < self.items[smaller_index]:
                break

            # Move the node down the heap
            self.swap(index, smaller_index)
            index = smaller_index

class MaxHeap(Heap):
    """
    Implementation of a MaxHeap 
    """

    def sift_up(self) -> None:
        """
        When a MaxHeap needs to sift_up after add(),
        1. Start from last element
        1. Swap node with parent while the parent is less than the node
        """
        # Start with last element
        index: int = len(self.items) - 1
        while self.has_parent(index) and self.get_parent(index) < self.items[index]:
            parent_index: int = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def sift_down(self) -> None:
        """
        When a MaxHeap needs to sift_down after pop(),
        1. Start from root node
        2. Swap node with the smallest child while the node is less than both children
        """
        # Start with root element
        index: int = 0

        # We make this the loop as if it no longer has a left child,
        # it will be a leaf node since a heap must be a complete binary tree
        while self.has_left_child(index):

            # Get the index of the largest child
            larger_index: int = self.get_left_child_index(index)
            if self.has_right_child(index) and (self.get_right_child(index) > self.get_left_child(index)):
                larger_index = self.get_right_child_index(index)

            # If the current item is larger than the of its children
            # then we have restored the heap property and the node is in its corerct
            # place in the heap
            if self.items[index] > self.items[larger_index]:
                break

            # Move the node down the heap
            self.swap(index, larger_index)
            index = larger_index


if __name__ == "__main__":

    # Using our heaps
    min_heap = MinHeap()
    arr: list = [5, 2, -1, 7, 7, 0, 11]
    for val in arr:
        min_heap.add(val)

    print("Min Heap")
    while len(min_heap):
        print(min_heap.pop())
    # Empty now
    print()

    max_heap = MaxHeap()
    for val in arr:
        max_heap.add(val)

    print("Max Heap")
    while len(max_heap):
        print(max_heap.pop())
    # Empty now
    print()

    # Using heapq heaps
    # heapq by default only creates a min heap implementation
    # to use a max heap, invert the values of the integers
    # heapify is faster than continually adding with heappush

    print("heapq Min Heap")
    heapq_min_heap: list = [val for val in arr]
    heapq.heapify(heapq_min_heap)
    while heapq_min_heap:
        print(heapq.heappop(heapq_min_heap))
    print()

    print("heapq Max Heap")
    heapq_max_heap: list = [-val for val in arr]
    heapq.heapify(heapq_max_heap)
    while heapq_max_heap:
        print(
            -heapq.heappop(heapq_max_heap))
