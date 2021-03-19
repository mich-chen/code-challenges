from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindrome(head: ListNode) -> bool:
    # base case
    if not head:
        return True

    slow = fast = head
    # find middle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # add second half to stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # compare two halves
    while stack:
        if stack.pop() != head.val:
            return False
        head = head.next

    return True
    
    # ***** O(1) Space complexity *****
    # same code for base case and finding middle

    # reverse second half in place
    half = None
    while slow:
        temp = slow.next
        slow.next = half
        half = slow
        slow = temp

    # compare halves
    while half:
        if half.val != head.val:
            return False
        half = half.next
        head = head.next

    return True
