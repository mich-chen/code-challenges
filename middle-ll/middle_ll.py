from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(self, head: ListNode) -> ListNode:

    # using hashmap to solve
    # base case, only 1 node in ll
    if not head.next:
        return head

    length = 1
    d = {}
    current = head
    while current:
        d[length] = current
        length += 1
        current = current.next

    # + 1 to mid length because dictionary keys start at 1
    return d[(len(d) // 2) + 1]

# **** using Array *****

    lst = []
    current = head
    while current: # until tail and checking most recently added node
        lst.append(current)
        current = current.next
    # find middle or second middle with // because array 0-indexing
    return lst[len(lst) // 2]

# **** slow - fast pointer *****
    
    # slow moves one, fast moves 2 steps ahead
    slow = fast = 0

    # check if current fast and fast's next is not None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


