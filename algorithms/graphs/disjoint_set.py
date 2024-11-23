#pylint: disable=all

"""
A disjoint set is sets that share no values in common.
This module implements the UnionFind class, which implements disjoint sets and
the two main methods find() and union().
UnionFind has many applications in graph problems.
"""

class UnionFindQF:
    """
    Implements Union Find with Quick Find
    """
    def __init__(self, size: int) -> None:
        """
        size: the number of vertices
        Time: O(n)
        """
        self.root: list[int] = [i for i in range(size)]

    def find(self, x: int) -> int:
        """
        Return the root of x
        Quick Find implementation
        Time: O(1)
        """
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        """
        Combine two vertices and update their roots
        Time: O(n) where n is size of root
        """
        x_root: int = self.find(x)
        y_root: int = self.find(y)

        if x_root != y_root:
            for i in range(len(self.root)):
                if self.root[i] == y_root:
                    self.root[i] = x_root

        return
    
    def connected(self, x: int, y: int) -> bool:
        """
        Return if two vertices are connected
        Time: O(1)
        """
        return self.find(x) == self.find(y)

class UnionFindQU:
    """
    Implements Union Find with Quick Union
    """
    def __init__(self, size: int) -> None:
        """
        size: the number of vertices
        Time: O(n)
        """
        self.root: list[int] = [i for i in range(size)]

    def find(self, x: int) -> int:
        """
        Return the root of x
        Time: O(n)
        """
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int) -> None:
        """
        Combine two vertices and update their parents
        Implements Quick Union
        Time: O(n) - because need to call find twice
        """
        x_root: int = self.find(x)
        y_root: int = self.find(y)

        if x_root != y_root:
            self.root[y_root] = x_root
        
        return

    def connected(self, x: int, y: int) -> bool:
        """
        Return if two vertices are connected
        Time: O(n)
        """
        return self.find(x) == self.find(y)

class UnionFindUBR:
    """
    Union Find with Union by Rank
    This is similar to Quick Union, but uses a rank for each vertex
    as to decide which vertex becomes the parent.
    In this case, the vertex with the higher rank will be chosen as the parent.
    This leads to a balanced tree, resulting in quicker finds.
    """
    def __init__(self, size: int) -> None:
        """
        size: the number of vertices
        Time: O(n)
        """
        self.root: list[int] = [i for i in range(size)]
        self.rank: list[int] = [0 for _ in range(size)]

    def find(self, x: int) -> int:
        """
        Return the root of x
        Time: O(log n) - because tree is balanced
        """
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int) -> None:
        """
        Combine two vertices and update their parents
        Implements Union by Rank
        Time: O(log n) - because need to call find twice
        """
        x_root: int = self.find(x)
        y_root: int = self.find(y)

        if x_root != y_root:
            # x_root has a higher rank, so make it the parent of y_root
            if self.rank[x_root] > self.rank[y_root]:
                self.root[y_root] = x_root
            # y_root has a higher rank, so make it the parent of x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.root[x_root] = y_root
            # their ranks are the same, so we just default to making x_root the parent
            else:
                self.root[y_root] = x_root
                self.rank[x_root] += 1      # Increment the rank of x_root
        
        return

    def connected(self, x: int, y: int) -> bool:
        """
        Return if two vertices are connected
        Time: O(log n)
        """
        return self.find(x) == self.find(y)

class UnionFind:
    """
    This is an optimized Union Find with Union by Rank and Path Compression
    """
    def __init__(self, size: int) -> None:
        """
        size: the number of vertices
        Time: O(n) - loop over arrays
        """
        self.root: list[int] = [i for i in range(size)]
        self.rank: list[int] = [1 for _ in range(size)]

    def find(self, x: int) -> int:
        """
        Return the root of x
        Time: O(a(n)) Amortized - where a(n) is Inverse Ackermann Function
        This implements Path Compression

        When traversing to find the root, it also finds and computes
        the root for all parent nodes along the path and updates their root
        nodes once the root is found
        """
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        """
        Combine two vertices and update their parents
        Implements Union by Rank
        Returns a bool based upon whether or not it tries to union
        two values that belong to the same set / have same parent.
        This results in creating a cycle in a graph.

        Returns True if the two values belong to the same set / have same parent.
            This operation does not change the rank/root of either x nor y.
        Returns False is the two values do not already belong to the same set.
            Will update x and y ranks and roots.

        Time: O(a(n)) Amortized - where a(n) is Inverse Ackermann Function
        """
        x_root: int = self.find(x)
        y_root: int = self.find(y)

        if x_root == y_root:
            return True

        # x_root has a higher rank, so make it the parent of y_root
        if self.rank[x_root] > self.rank[y_root]:
            self.root[y_root] = x_root
        # y_root has a higher rank, so make it the parent of x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.root[x_root] = y_root
        # their ranks are the same, so we just default to making x_root the parent
        else:
            self.root[y_root] = x_root
            self.rank[x_root] += 1      # Increment the rank of x_root

        return False

    def connected(self, x: int, y: int) -> bool:
        """
        Return if two vertices are connected
        Time: O(a(n)) Amortized - where a(n) is Inverse Ackermann Function
        """
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    # Test Case - Quick Find
    uf = UnionFindQF(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
    print()

    # Test Case - Quick Union
    uf = UnionFindQU(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
    print()

    # Test Case - Union by Rank
    uf = UnionFindUBR(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
    print()

    # Test Case - Union Find Optimized
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
    print()