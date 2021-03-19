from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumRootToLeaf(root: TreeNode) -> int:

    """
    Using int(string, base) to convert string of number and base 2
    """
        
        # base case if tree only 1 node
        if not root.left and not root.right:
            return int(str(root.val), 2)
        
        # keep track of all the string binaries
        binaries = []
        
        # helper DFS function
        def dfs(node, string):
            if node:
                # concatenate current value to the input string
                current = string + str(node.val)
                # if node is a leaf
                if not node.left and not node.right:
                    # append the completed binary string to list
                    binaries.append(current)
                # if not a leaf, look at children
                else:
                    dfs(node.left, current)
                    dfs(node.right, current)
        # start recursion at root and an empty string
        dfs(root, '')

        return sum(int(string,2) for string in binaries)

# **** test cases ****
# sumRootToLeaf([1,0,1,0,1,0,1]) --> 22
# (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
