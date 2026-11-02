# Reverse Linked List
# status: solo | retry: -
# note: retry passed, iterative: save nxt = cur.next, point cur.next back to prev, step prev/cur forward;
# prev is the new head when cur hits None, O(n) time O(1) space

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
