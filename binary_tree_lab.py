from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """Return the maximum depth (height) of a binary tree.

    Depth is the number of nodes along the longest path from the root down
    to the farthest leaf. An empty tree has depth 0.

    Approach:
        Recursive post-order traversal. The depth of a tree is one (for the
        current node) plus the larger of the depths of its left and right
        subtrees. The base case is an empty subtree, which has depth 0.

    Complexity:
        Time:  O(n) - every node is visited exactly once.
        Space: O(h) - recursion stack, where h is the tree height. This is
               O(log n) for a balanced tree and O(n) for a skewed tree.
    """
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Return the lowest common ancestor (LCA) of nodes p and q in a BST.

    The LCA is the deepest node that has both p and q as descendants, where
    a node counts as a descendant of itself. Assumes p and q exist in the tree.

    Approach:
        Use the BST ordering property and walk down from the root:
        - If both p and q are smaller than the current node, the LCA must be
          in the left subtree.
        - If both are larger, the LCA must be in the right subtree.
        - Otherwise p and q split here (or one of them is the current node),
          so the current node is the LCA.
        This is written as a loop rather than recursion, since each step only
        ever moves to a single child.

    Complexity:
        Time:  O(h) - at most one node per level is visited, where h is the
               tree height (O(log n) balanced, O(n) skewed).
        Space: O(1) - only a single pointer is tracked.
    """
    node = root
    while node is not None:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
    return node
