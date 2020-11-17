from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root: TreeNode) -> bool:

    if not root:
        return True

    def isMirror(left, right):
        # base case
        if not left and not right:
            return True
        if not left or not right:
            return False

        # if same values, recurse on mirrored pairs
        if left.val == right.val:
            outpair = isMirror(left.left, right.right)
            inpair = isMirror(left.right, right.left)
            return outpair and inpair
        else:
            return False

    return isMirror(root.left, root.right)

