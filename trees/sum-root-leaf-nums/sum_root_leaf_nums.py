# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(node, number):
            if node:
                # if at leaf, return the root-to-leaf number
                if not node.left and not node.right:
                    return number * 10 + node.val

                # sum left and right root-to-leaf path numbers
                return dfs(node.left, number * 10 + node.val) + dfs(node.right, number * 10 + node.val)

            return 0

        return dfs(root, 0)
        