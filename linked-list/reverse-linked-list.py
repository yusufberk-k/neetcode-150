# Reverse Linked List
# status: hint | retry: 2026-10-29
# note: first linked list problem; had to learn what a linked list is. iterative: save nxt = cur.next,
# point cur.next back to prev, step prev/cur forward; prev is the new head when cur hits None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = head

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
