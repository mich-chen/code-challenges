# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """Recrusively - DFS"""
        def dfs(node, number):
            if node:
                # if at leaf, return the root-to-leaf number
                if not node.left and not node.right:
                    return number * 10 + node.val

                # sum left and right root-to-leaf path numbers
                return dfs(node.left, number * 10 + node.val) + dfs(node.right, number * 10 + node.val)

            return 0

        return dfs(root, 0)

    def sumNumbers_iterative(self, root: TreeNode) -> int:
        """Iteratively - DFS- Stack"""
        # stack to store tuple of (node, root-to-leaf path num)
        stack = [(root, 0)]
        total = 0
        while stack:
            node, num = stack.pop()
            # if leaf
            if not node.left and not node.right:
                total += (num * 10 + node.val)
            if node.right:
                stack.append((node.right, num * 10 + node.val))
            if node.left:
                stack.append((node.left, num * 10 + node.val))
        return total
        