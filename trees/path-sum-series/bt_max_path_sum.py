# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # gloabl total max sum
        self.sum = float('-inf')

        # post order traversal
        def dfs(node):
            if not node:
                return 0
            # gather sums from all left and right children
            # only gather positive values from children because looking for max
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            # compare current largest with current path (self + children)
            self.sum = max(self.sum, node.val + left + right)
            # only return largest sum of children (for max path)
            return node.val + max(left, right)
        
        dfs(root)
        return self.sum
