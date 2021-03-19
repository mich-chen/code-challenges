# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
def averageOfLevels(root: TreeNode) -> List[float]:

    # BFS
    output = []
    # queue of tuples for node
    queue = collections.deque([root])
    
    while queue:
        avg = 0
        temp = []
        length = len(queue)
        for i in range(len(queue)):
            current = queue.popleft()
            avg += current.val
            if current.left:
                temp.append(current.left)
            if current.right:
                temp.append(current.right)
        output.append(avg / length)
        queue.extend(temp)
        
    return output


    """
    # ***** DFS *****
    output = []
    tracker = {} 
    
    def dfs(root, level):
        # base case
        # if empty tree
        if not root:
            return
        
        tracker.setdefault(level, [])
        tracker[level].append(root.val)
        dfs(root.left, level + 1) 
        dfs(root.right, level + 1) 
        
    dfs(root, 0)
    # print(tracker)
    for i in range(len(tracker)):
        length = len(tracker[i])
        avg = sum(num for num in tracker[i]) / length
        output.append(avg)
    
    return output
    """


# ***** Test cases *****
# Input: [3,9,20,15,7]
# Output: [3, 14.5, 11]