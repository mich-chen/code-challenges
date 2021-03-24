# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import TreeNode, List
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:


# ------------------------------------------------------------------------------


        # iterative - condensed, loops through level list
        #           - use -1 as direction for list slicing for reversing
        if not root:
            return []

        q = deque([root])
        result = []
        direction = 1

        while q:
            lvl = []
            # iterates through current queue (current level)
            for i in range(len(q)):
                node = q.popleft()
                # add node value to levels list
                lvl.append(node.val)
                # traverse, new level in queue will evaluate length at next while-loop iteration
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # add lvl to result in forward or reverse using direction and slicing
            result.append(lvl[::direction])
            direction *= (-1)
        
        return result

# ------------------------------------------------------------------------------

        # iterateively - initial attempt, no nested loops
        if not root:
            return []

        q = deque([root])
        lvl = []
        current = []
        result = [[root.val]]
        to_reverse = True

        while q:
            node = q.popleft()
            # if at leaf
            if not node or (not node.left and not node.right):
                if len(q) == 0 or len(current) > 0:
                    # add level nodes to queue
                    q.extend(lvl)
                    if to_reverse:
                        current.reverse()
                    to_reverse = not to_reverse
                    result.append(current)
                    # reset current and lvl
                    current = lvl = []
                continue

            # traverse
            if node.left:
                current.append(node.left.val)
                lvl.append(node.left)
            if node.right:
                current.append(node.right.val)
                lvl.append(node.right)
            
            # when finished traversing through queue, add new level to queue
            if len(q) == 0:
                q.extend(lvl)
                if to_reverse:
                    current.reverse()
                    lvl.reverse()
                to_reverse = not to_reverse
                result.append(current)
                # reset current and lvl
                current = lvl = []

        return result
