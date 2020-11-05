from typing import List, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def binaryTreePaths(root: TreeNode) -> List[str]:

    if not root:
        return []

    def dfs(node, path, output):
        if node:
            # if leaf, add leaf to string path and add to output array
            if not node.left and not node.right:
                path += str(node.val)
                output.append(path)
                return
            # not leaf, concatenate current node to path string with arrow
            path += str(node.val) + '->'
            dfs(node.left, path, output)
            dfs(node.right, path, output)

    result = []
    dfs(root, '', result)
    
    return result