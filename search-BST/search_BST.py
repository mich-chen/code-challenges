from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def searchBST(root: TreeNode, val: int) -> TreeNode:
        
    if not root:
        return []
    
    queue = collections.deque([root])
    
    while queue:
        current = queue.popleft()
        if current:
            if current.val == val:
                return current
            if current.val < val:
                queue.append(current.right)
            if current.val > val:
                queue.append(current.left)