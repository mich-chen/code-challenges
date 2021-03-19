from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def hasPathSum(root: TreeNode, sum: int) -> bool:

    if not root:
        return False

    def dfs(node, sum, target):
        if node:
            # if leaf, check if sum == target
            if not node.left and not node.right:
                if (sum + node.val) == target:
                    return True

            # continue until leaf, add current value to sum
            return dfs(node.left, sum + node.val, target) or dfs(node.right, sum + node.val, target)

        return dfs(root, 0, sum)


if __name__ == '__main__':
    
    hasPathSum([5,4,8,11,null,13,4,7,2,null,null,null,1], 22) # True