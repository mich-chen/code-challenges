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