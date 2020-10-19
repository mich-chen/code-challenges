from typing import TreeNode

def maxDepth(root: TreeNode) -> int:
        
    # ***** Recursion DFS *****
    # base case 
    if not root:
        return 0
    
    # if node, 1 + the maximum between its left and right children
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
***** DFS iterative solution ******

stack = [(root, 1)]
depth = 0
while stack:
    node, length = stack.pop()
    if node:
        # update depth to be max between current depth or new length
        depth = max(depth, length)
        # DFS on children, and increment length 
        if node.left:
            stack.append((node.left, legnth + 1))
        if node.right:
            stack.append((node.right, length + 1))
return depth
'""