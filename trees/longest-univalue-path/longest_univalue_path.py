class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longestUnivaluePath(root: TreeNode) -> int:
    
    # if empty treenode
    if not root:
      return 0
   
    # self attribute so helper dfs function can access
    self.maxlength = 0

    def dfs(node, parent_val):
       
        # base case
        if not node:
            return 0

        # recursively call dfs on all left and right branches
        left = dfs(node.left, node.val)
        right = dfs(node.right, node.val)
        # update maxlength
        self.maxlength = max(self.maxlength, left + right)

        # if matching node values, return 1 + the side with longest length
        if node.val == parent_val:
            return 1 + max(left, right)
        else:
            return 0
   
    dfs(root, None)
    return self.maxlength


if __name__ == '__main__':
  
    longestUnivaluePath([])  # 0
    longestUnivaluePath([5,4,5,1,1,5])  # 2