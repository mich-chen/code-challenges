from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pathSum(root: TreeNode, sum: int) -> int:
    """Recursion with prefix sum."""

    if not root:
        return 0

    def dfs(node, sum, target, prefix):
        if node:
            # update sum with current node's value
            sum += node.val
            # difference between sum and target is prefix
            # if prefix exists set as result, else 0
            result = prefix.get(sum - target, 0)
            # add current sum to prefix dict as new key
            prefix.setdefault(sum, 0)
            prefix[sum] += 1
            # add all children's results
            result += dfs(node.left, sum, target, prefix)
            result += dfs(node.right, sum, target, prefix)
            # remove current sum from prefix dict after pop off call stack
            # need to remove after recursion because goes from bottom to top
            prefix[sum] -= 1
            return result
        # if leaf or None
        else:
            return 0

    # instantiate prefix sum dict with 0: 1
    prefix = {0: 1}
    return dfs(root, 0, sum, prefix)


if __name__ == '__main__':
    
    pathSum([1, -2, -3], -1) # 1
    pathSum([10,5,-3,3,2,null,11,3,-2,null,1], 8) # 3
