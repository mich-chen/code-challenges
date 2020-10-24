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
    
    def dfs(node, depth, parent, x, y):
        if node:
            if node.val == x or node.val == y:
                parents[node.val] = parent
                depths[node.val] = depth
            dfs(node.left, depth + 1, node, find)
            dfs(node.right, depth + 1, node, find)
        else:
            return
        
    dfs(root, 0, TreeNode(), x, y)
    return parents[x] != parents[y] and depths[x] == depths[y]