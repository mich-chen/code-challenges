from typing import List, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output = []
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """refacctoring recursive solution"""
        def dfs(node, path):
            if node:
                # at leaf, add path to output
                if not node.left and not node.right:
                    path = '->'.join(path + [str(node.val)])
                    self.output.append(path)
                    return
                # traverse
                dfs(node.left, path + [str(node.val)])
                dfs(node.right, path + [str(node.val)])
            
        # base case constraint: root only contains one node
        self.output = [] # reset class attribute for each new instance of class
        dfs(root, [])
        return self.output

# ------------------------------------------------------------------------------

def binaryTreePaths(root: TreeNode) -> List[str]:

    # DFS recursively
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

    """
    **** DFS Iteratively with Stack ****
    if not root:
        return []

    stack = [(root, '')]
    result = []
    while stack:
        current, path = stack.pop()

        # if leaf, add value to path and to result
        if not current.left and not current.right:
            path += str(node.val)
            result.append(path)
        
        # if not leaf, concatenate path with arrow and add children to stack
        path += str(node.val) + '->'
        if current.left:
            stack.append((current.left, path))
        if current.right:
            stack.append((current.right, path))

    return result
    """