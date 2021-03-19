# Definition for a Node.
class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Node') -> 'Node':

    # if head == []
    if not head:
        return head   # return []

    # DFS approach --> multilevel dll represents tree
    # when node has child, then represents tree branching and a new edge
    # when node.next == None, represents a leaf

    # ***** DFS Iteratively *****
    stack = [head]
    # to update and keep track of new previouses
    prev = Node(0)  # initialize as a new empty(0) Node for algorithm

    while stack:
        current = stack.pop()
        # reassign node's attributes
        current.prev = prev
        # update prev.next to be current, in case current node may have been a child
        prev.next = current
        # update prev to be current node so next node's prev will be this current node
        # to keep track of beginning's correct order
        prev = current
        # append next node first to stack
        if current.next:
            stack.append(current.next)
        # append next node's child to stack last so it will be popped first
        if current.child:
            stack.append(current.child)
            # to make this a valid dll, child will be set to None
            current.child = None

    head.prev = None # reset head's prev to none instead of the intialized empty(0) node
    return head


if __name__ == '__main__':
    
    print(flatten([1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]))
    # [1,2,3,7,8,11,12,9,10,4,5,6]
    print(flatten([]))  # []
    print(flatten([1,2,None,3]))  # [1,3,2]
