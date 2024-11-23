#pylint: disable=all

"""
Taken from Leetcode 146
"""

class ListNode:
    def __init__(self, key: int, val: int) -> None:
        self.key: int = key
        self.val: int = val
        self.prev = None
        self.next = None
        

class DLL:
    """
    A doubly-linked list class with the add and remove methods
    Very simple class
    """
    def __init__(self) -> None:
        self.head: ListNode = ListNode(-1, -1)
        self.tail: ListNode = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def add(self, node: ListNode) -> None:
        """
        Add the node to the end of the list
        """
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        self.size += 1

        return

    def remove(self, node: ListNode) -> None:
        """
        Remove the node from the list
        """
        # Can't remove from an empty list
        if self.size == 0:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

        return


class LRUCache:
    """
    Create a Least Recently Used Cache
    The get and put operations occur in O(1) time
    When the capacity is exceeded, evict the last accessed value from the cache
    The LRU item is at the head of the DLL. The most recently used is at the tail.
    """
    def __init__(self, capacity: int) -> None:
        self.dll: DLL = DLL()
        self.lookup: dict[int, ListNode] = {}
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        """
        Get the value given a key. If it doesn't exist, return -1
        """
        if key not in self.lookup:
            return -1

        found_node: ListNode = self.lookup[key]
        # Remove node and move to end
        self.dll.remove(found_node)
        self.dll.add(found_node)

        return found_node.val

    def put(self, key: int, val: int) -> None:
        """
        Add a new key value pair into the cache
        """
        if key in self.lookup:
            self.dll.remove(self.lookup[key])

        new_node: ListNode = ListNode(key, val)
        self.lookup[key] = new_node
        self.dll.add(new_node)

        if len(self.dll) > self.capacity:
            del self.lookup[self.dll.head.next.key]
            self.dll.remove(self.dll.head.next)

        return


if __name__ == "__main__":
    lru: LRUCache = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)

    print(lru.get(1))   # print 1
    print(lru.get(2))   # print 2
    
    lru.put(3, 3)       # 1 gets evicted
    print(lru.get(1))   # Should be -1
