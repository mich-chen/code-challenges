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
        
        def recurse(node):
        # preorder traversal
            if node:
                left = node.left
                right = node.right
                if not self.prev:
                    self.prev = node
                else:
                    self.prev.right = node
                    self.prev.left = None
                    self.prev = node
                
                # left
                recurse(left) # 2 -> 3 -> None
                # right
                recurse(right)
            else:
                return
                
        # prev = [TreeNode(0)]
        recurse(root)
        return root
        