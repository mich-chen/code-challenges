from typing import List, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pathSum(root: TreeNode, sum: int) -> List[List[int]]:

    if not root:
        return []

    def dfs(node, path, sum, target, output):
        if node:
            # if leaf, check if sum is equal to target sum
            if not node.left and not node.right:
                sum += node.val
                if sum == target:
                    # add current leaf to path and append to output
                    output.append(path + [node.val])

            # not leaf --> add to sum, add to path, and dfs to children
            dfs(node.left, path + [node.val], sum + node.val, target, output)
            dfs(node.right, path + [node.val], sum + node.val, target, output)

    result = []
    dfs(root, [], 0, sum, result)

    return result


if __name__ == '__main__':
    
    pathSum([5,4,8,11,null,13,4,7,2,null,null,5,1], 22)  # [[5,4,11,2],[5,8,4,5]]

