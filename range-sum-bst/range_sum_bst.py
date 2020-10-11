from typing import List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    """Return sum of all nodes that are within left and right range, inclusively."""

    # DFS iteratively
    stack = [root]
    total_sum = 0

    while stack:
        current = stack.pop()

        if current:
            # if current node falls between L and R range
            # then add current node's children to stack
            if current.val > L:
                stack.append(current.left)
            if current.val < R:
                stack.append(current.right)

            # if current node's val falls between L and R range
            # then add to total_sum
            if L <= current.val <= R:
                total_sum += current.val

    return total_sum
