from typing import ListNode

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    # if both are empty lls
    if (l1 is None) and (l2 is None):
        return None
    
    # instantiate a new node as pointer for new ll
    current = ListNode(0) 
    # keep track of head of new ll 
    new_sorted = current  
    
    # merge sorted lls until one is finished
    while l1 and l2:
        # set node as next in new ll for whichever node has smaller value
        if (l1.val > l2.val):
            current.next = l2
            l2 = l2.next
        else: # (l1.val < l2.val)
            current.next = l1
            l1 = l1.next
        # move pointer in new ll
        current = current.next
    
    # set the rest of current.next to be the remainder of the unfinished list
    # if end of a ll, l1 or l2 will be None (falsey)
    current.next = l1 or l2
    
    return new_sorted.next