from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    
    if t1 is None:
        return t2
    
    if t2 is None:
        return t1
    
    # create new merged tree by summing t1 and t2 as new node's value
    new = TreeNode(t1.val + t2.val)
    # recursively call function on current node's left and right
    new.left = self.mergeTrees(t1.left, t2.left)
    new.right = self.mergeTrees(t1.right, t2.right)
    
    return new


if __name__ == '__main__':
    
    print(mergeTrees([2,1,3,null,4,null,7]))  # [3,4,5,5,4,null,7]