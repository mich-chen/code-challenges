from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isCousins(root: TreeNode, x: int, y: int) -> bool:
    
    """
    cousins = same depth, different parent nodes
    """
    # base case, at least 2 nodes
    if not root.left or not root.right:
        return False
    
    parents = {x: None, y: None}
    depths = {x: 0, y: 0}
    
    def dfs(node, depth, parent, find):
        if node:
            if node.val == find:
                parents[find] = parent
                depths[find] = depth
            else:
                dfs(node.left, depth + 1, node, find)
                dfs(node.right, depth + 1, node, find)
        else:
            return
        
    dfs(root, 0, TreeNode(), x)
    dfs(root, 0 ,TreeNode(), y)
    return parents[x] != parents[y] and depths[x] == depths[y]