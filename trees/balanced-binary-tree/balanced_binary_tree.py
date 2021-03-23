# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node):
        """Postorder traversal - using integer as indicator."""
        if not node:
            return 0

        left = self.traverse(node.left)
        # exit traversal early if unbalanced
        if left == -1:
            return -1
        right = self.traverse(node.right)
        # exit traversal early if unbalanced
        if right == -1:
            return -1
        # either return -1 or max height of branch
        # -1 is to indicate unbalanced
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)

    def bool_traverse(self, node):
        """Postorder traversal - use pair of height, boolean as indicator."""
        if not node:
            return (0, True)
        
        left = self.bool_traverse(node.left)
        # exit traversal early if unbalanced
        l_height, l_isBalanced = left
        if not l_isBalanced:
            return (l_height + 1, False)

        right = self.bool_traverse(node.right)
        # exit traversal early if unbalanced
        r_height, r_isBalanced = right
        if not r_isBalanced:
            return (r_height + 1, False)

        if abs(l_height - r_height) > 1:
            return (1 + max(l_height, r_height), False)
        
        return (1 + max(l_height, r_height), True)

    def isBalanced(self, root: TreeNode) -> bool:
        
        print(self.traverse(root) != -1)
        print(self.bool_traverse(root)[1])

        # return self.traverse(root) != -1
        # return self.bool_traverse(root)[1]

if __name__ == '__main__':

    # Tree is set up through leetcode 
    Solution().isBalanced([3,9,20,None,None,15,7]) # True
    Solution().isBalanced([1,2,2,3,3,None,None,4,4]) # False
