from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def postorder(root: 'Node') -> List[int]:
    """deal with left, then right, then self"""
    
    output = []
    
    def recurse(node):
        if not node:
            return
        if node:
            # children is list of nodes
            for child in node.children:
                recurse(child)
            output.append(node.val)
    
    recurse(root)
    return output
    