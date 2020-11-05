from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        # using a class attribute
        self.prev = None
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        def recurse(node, prev):
        # preorder traversal
            if node:
                left = node.left
                right = node.right
                prev[0].right = node
                prev[0].left = None
                prev[0] = node
                
                # left
                recurse(left, prev) # 2 -> 3 -> None
                # right
                recurse(right, prev)
            else:
                return
                
        prev = [TreeNode(0)]
        recurse(root, prev)
        return root
        