from typing import List, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    
    if nums:
        mid = len(nums) // 2 # middle index, the root
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

# test case
# sortedArrayToBST([-10,-3,0,5,9]) --> [0,-3,9,-10,null,5]
