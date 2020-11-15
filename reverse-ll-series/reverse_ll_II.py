from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:

    if not head or m == n:
        return head

    temp = ListNode(0)
    temp.next = head
    front = temp
    # iterate through ll until at position m
    for i in range(m - 1):
        front = front.next

    # instantiate variables for reversing
    rev = None
    current = front.next
    tail = front.next
    # iterate from position m to n, inclusive of position m and n
    for i in range(n - m + 1):
        # reverse
        next = current.next
        current.next = rev
        current, rev = next, current

    # reconnect reversed portion to original
    front.next = rev
    tail = current

    return temp.next # temp was tracking original head
