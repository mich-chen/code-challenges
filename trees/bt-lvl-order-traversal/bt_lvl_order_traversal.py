from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

def levelOrder(root: TreeNode) -> List[List[int]]:

    if not root:
        return []

    # store tuples of node and level
    q = deque([(root, 0)])
    output = {}

    while q:
        current, level = q.popleft()
        if current:
            if level not in output:
                output.setdefault(level, [])
            output[level].append(current.val)
            if current.left:
                q.append((current.left, level + 1))
            if current.right:
                q.append((current.right, level + 1))

    return list(output.values())


if __name__ == '__main__':
    
    levelOrder([3,9,20,null,null,15,7]) # [[3],[9,20],[15,7]]
