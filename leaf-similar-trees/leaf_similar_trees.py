from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    """
    leaf sequence: left --> right
    two binary trees are considered leaf-similar if leaf sequence is same
    return True only if same leaf sequence
    """
    
    leaves1 = []
    leaves2 = []
    
    # leaf sequence is left to right
    def dfs(node, leaf_list):
        if node:
            # if node is leaf
            if not node.left and not node.right:
                leaf_list.append(node.val) 
                
            dfs(node.left, leaf_list) 
            dfs(node.right, leaf_list) 

    dfs(root1, leaves1) 
    dfs(root2, leaves2) 
    return leaves1 == leaves2

# Test cases
# leafSimilar([1,2,3], [1,3,2]) --> False

