from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: ListNode) -> ListNode:

    current = head
    prev = None

    while current:
        next = current.next
        current.next = prev
        current, prev = next, current

    return prev


