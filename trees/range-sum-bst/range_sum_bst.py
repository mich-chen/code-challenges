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


    """

    *** Alternative solution: DFS + Recursion ***

    # base cases
    if not root:
        return 0

    total_sum = 0

    # if current node falls within L and R range, add to total sum
    if L <= root.val <= L:
        total_sum += 1

    # call function on all left and right children and add their sums
    total_sum += rangeSumBST(root.left, L, R)
    total_sum += rangeSumBST(root.right, L, R)

    return total_sum

    """

# **** Tests *****

# print(rangeSumBST([10,5,15,3,7,null,18], 7, 15))  # 32

