from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def preorder(root: 'Node') -> List[int]:
    """preorder is self, left, right"""

    output = []

    def recurse(node):
        if node:
            output.append(node.val)
            # children are list of nodes
            for child in node.children:
                recurse(child)

    recurse(root)
    return output

# ***** Iteratively ******
"""
    output = []
    stack = [root]

    while stack:
        current = stack.pop()
        output.append(current.val)
        for child in current.children[::-1]:
            stack.append(child)

    return output
"""
