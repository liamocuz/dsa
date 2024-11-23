#pylint: disable=all

"""
Taken from Leetcode 105
"""

class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    This is a much faster version to build the tree
    The speed improvements come from making the root node index lookup in the inorder array 
    using a dict with O(1) lookup instead of O(n) at each level as well as not taking slices
    of arrays when recursing
    The memory improvements come from not taking slices at each recurrence and instead maintaining
    array integer pointers
    """
    # Idea: Same as below, but using integers and better lookup
    #       preorder is formatted as so -> [root, left..., right...]
    #       inorder is formatted as so -> [left..., root, right...]

    # Time: O(n)
        # Loop for indices, and only move through rest of array once with pointers
    # Space: O(n)
        # Store in dict, recurse up to n times
    if not preorder or not inorder:
        return None

    # Create a dict to make index lookup of the root easy
    indices: dict[int, int] = {}
    for i, val in enumerate(inorder):
        indices[val] = i

    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode:
        if pre_start > pre_end:
            return None

        # The root val of a subtree will always be the first value in the preorder subarray
        root_val: int = preorder[pre_start]
        root: TreeNode = TreeNode(root_val)

        # Find where the root is in the inorder array
        # To the left will be the left subtree, to the right will be the right subtree
        mid_index: int = indices[root_val]
        # Find how large the left subtree array is in inorder
        left_size: int = mid_index - in_start

        # Recurse by updating the index pointers
        # Preorder
            # left [pre_start + 1, pre_start + left_size]
            # right [pre_start + left_size + 1, pre_end]
        # Inorder - leaves the mid index out as that is the subtree root
            # left [in_start, mid_index - 1]
            # right [mid_index + 1, in_end]
        root.left = build(pre_start + 1, pre_start + left_size, in_start, mid_index - 1)
        root.right = build(pre_start + left_size + 1, pre_end, mid_index + 1, in_end)

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    This is a slower but more easily understandable version
    """
    # Idea: Recursively build the tree by finding the root node at each subtree
    #       The root node can always be found as the first value in the preorder array
    #       Then the left and right subtrees can be found by finding the index of the root
    #       in the inorder traversal which splits the tree in half
    #       Take slices of each array for the left and right subtrees after finding how
    #       big the two subtrees are from the indorder array

    # Time: O(n^2)
        # Need to find mid at every evel
    # Space: O(n^2)
        # Taking slices at each level, which will be held in memory through the recursion

    if not preorder:
        return None

    # Create the root node
    root = TreeNode(preorder[0])
    # Find where the root node exists in the inorder array
    # Used to create the size of the next recursive arrays
    mid: int = inorder.index(preorder[0])

    root.left = self.buildTree(preorder[1: mid + 1], inorder[0: mid])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root


if __name__ == "__main__":
    
    root = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20 ,7])
