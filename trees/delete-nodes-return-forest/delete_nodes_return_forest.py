from typing import List, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def delNodes(root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

    """
    to_delete is list of node vals to remove from tree
    return a list of lists of new roots to leftover trees
    new roots are subtrees (disjoint)

    """
    
    if not root:
        return []

    if not to_delete:
        return root

    to_delete = set(to_delete) # distinct values
    output = []

    def dfs(node, parent, to_delete):
        # if new subtree: parent is in to_delete, self is not in to_delete
        # edge case: if orig root in to_delete, then parent == None
        if not node:
            return node
        if (parent == None or parent.val in to_delete) and node.val not in to_delete:
            output.append(node)
        node.left = dfs(node.left, node, to_delete)
        node.right = dfs(node.right, node, to_delete)
        return None if node.val in to_delete else node
        
    dfs(root, None, to_delete)
    return output


# **** dfs less clean *******

    # def dfs(node, parent, to_delete):
    #     if node:
    #     # delete node that is in to_delete
    #     # edge case: if root is in to_delete, then parent is None
    #         if node.val in to_delete and parent != None:
    #             if parent.left == node:
    #                 parent.left = None
    #             if parent.right == node:
    #                 parent.right = None
    #     # to know if new subtree:
    #     # current node is not in to_delete
    #     # and parent node is in to_delete
    #     # edge case: if root is in to_delete, then parent is None
    #     if (parent == None or parent.val in to_delete) and node not in to_delete:
    #         output.append(node)
    #     # continue to traverse
    #     dfs(node, parent, to_delete)
    #     dfs(node, parent, to_delete)

    # dfs(root, None, to_delete)
    # return output

