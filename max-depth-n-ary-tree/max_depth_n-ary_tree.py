"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def maxDepth(root: 'Node') -> int:
        
    if not root:
        return 0
    
    # if only one node in tree
    if not root.children:
        return 1

    return max([1 + maxDepth(child) for child in root.children])

# ***** add helper DFS function *****

    # def dfs(node):
        
        # for child in node.children:
        #     return max(1 + dfs(child))
        # # return max(1 + dfs(child) for child in node.children)
    
    # return dfs(root)

# **** add helper DFS function passing depth *****

    # def dfs(node, depth):
#       # if leaf
    #     if not node.children:
    #         return depth
    #     maximum = 1
    #     for child in node.children: 
    #         maximum = max(maximum, dfs(child, depth + 1))
    #     return maximum

# adding list comprehesion 
    # return max([dfs(child, depth + 1) for child in node.children])

