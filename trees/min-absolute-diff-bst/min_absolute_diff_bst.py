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

    def getMinDiff_inorder(self, root: TreeNode) -> int:
        """Recursively - inorder traversal."""

        def traverse(node, dp):
            if not node:
                return dp
            # inorder traversal --> left, self, right
            left = traverse(node.left, dp)
            min_diff = dp[1]
            # calculate min diff for children, if not at root
            #   self - left child (stored as dp[0])
            #   or self - right child
            if dp[0] != -1:
                min_diff = min(min_diff, node.val - dp[0])
            # update dp[0] as self for calculating self - right child
            dp[0], dp[1] = node.val, min_diff
            return traverse(node.right, dp)
        
        # store data as list where:
        #   list[0] = node to be subtracted
        #   list[1] = min diff
        dp = [-1, float('inf')]
        output = traverse(root, dp)
        return output[1]

