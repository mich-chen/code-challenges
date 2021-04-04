# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinDiff_hilo(self, root: TreeNode) -> int:
        """Recrusively - knowing hi and lo from BST to calculate."""
        def fn(node, lo, hi):
            if not node:
                return hi - lo # to calculate difference
            # BST --> left child is smaller than self, and right child greater
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))

    