from typing import TreeNode

def maxDepth(root: TreeNode) -> int:
        
    # ***** Recursion DFS *****
    # base case 
    if not root:
        return 0
    
    # if node, 1 + the maximum between its left and right children
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def maxDepth_recursive2(root: TreeNode) -> int:

    # ----- 2nd recursive DFS solution -----------------------
    # base case
    if not root:
        return 0
    
    def traverse(node, level):
        # if at leaf
        if not node or (not node.left and not node.right):
            return level
        left = traverse(node.left, level + 1)
        right = traverse(node.right, level + 1)

        return max(left, right)
    return traverse(root, 1)

"""
----- DFS iterative solution 2 ------

if not node:
    return 0
longest = 1
stack = [(root, 1)]
while stack:
    node, level = stack.pop()
    # if at leaf
    if not node or (not node.left and not node.right):
        longest = max(level, longest)
    else:
        stack.extend([(node.left, level + 1), (node.right, level + 1)])
return longest


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