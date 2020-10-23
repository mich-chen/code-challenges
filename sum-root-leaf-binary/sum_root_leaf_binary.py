from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumRootToLeaf(root: TreeNode) -> int:
        
        if not root.left and not root.right:
            return int(str(root.val), 2)
        
        binarys = []
        
        def dfs(node, string):
            if node:
                current = string + str(node.val)
                # if node is a leaf
                if not node.left and not node.right:
                    binarys.append(current)
                # if not a leaf, look at children
                else:
                    dfs(node.left, current)
                    dfs(node.right, current)
                    
        dfs(root, '')
        return sum(int(string,2) for string in binarys)