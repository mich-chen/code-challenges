import collections

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):

    if root is None:
        return 0

    # create a queue, consists of list of tuples
    # tuple is node and its correspending depth
    queue = collections.deque([(root, 1)])

    while queue:
        # pop from beginning of queue
        current, depth = queue.popleft()
        # if current node is not None
        if current:
            # if current node is a leaf reached min depth
            if not current.left and not current.right:
                return depth
            # if not at leaf, then continue to add to queue
            queue.append((current.left, depth + 1))
            queue.append((current.right, depth + 1))

    return depth

def minDepth_recursive(root):
    """Recursively BFS, min depth when hit first leaf."""
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    # reduce unnecessary traversals
    if not root.left:
        # add self as a count to depth
        return 1 + minDepth_recursive(root.right)
    if not root.right:
        # add self as a count to depth
        return 1 + minDepth_recursive(root.left)
    return 1 + min(minDepth_recursive(root.left), minDepth_recursive(root.right))


# Input: [3,9,20,null,null,15,7]
# Output: 2