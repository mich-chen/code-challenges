from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def deepestLeavesSum(root: TreeNode) -> int:

    # key is depth, value is sum of the nodes at that depth
    levels = {}

    def dfs(node, depth):
        if not node:
            return
        levels.setdefault(depth, 0)
        levels[depth] += node.val
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 1)
    # return sum at deepest level
    deepest = max(levels)
    return levels[deepest]


# test case
# deepestLeavesSum([1,2,3,4,5,null,6,7,null,null,null,null,8]) --> 15