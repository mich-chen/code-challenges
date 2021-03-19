from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def allPossibleFBT(N: int) -> List[TreeNode]:

    # cannot make valid full binary tree with even N
    if N % 2 == 0:
        return []

    def makeTree(n, dp):
        current = []
        # base case if n is 1, return list of one tree node
        if n <= 1:
            return [TreeNode(0)]
        # memoize
        if n in dp:
            return dp[n]
        # iterate through odd numbers from 1 to n
        for i in range(1, n, 2):
            # split all possibilities of nodes between left and right
            left = makeTree(i, dp)
            right = makeTree(n - i - 1, dp)

            for k in range(len(left)):
                for j in range(len(right)):
                    # build full binary tree, add to current list
                    new = Treenode(0)
                    new.left = left[k]
                    new.right = right[j]
                    current.append(new)
                    
        dp[n] = current
        return current

    return makeTree(N, {})