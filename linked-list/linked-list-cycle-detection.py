# Linked List Cycle
# status: hint | retry: 2026-11-01
# note: correct version is fast/slow pointers where fast moves two steps and slow moves one step
# each iteration; loop condition should check both cur and cur.next (while cur and cur.next)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: return False
        cur = head.next
        tail = head
        c = 0
        while cur.next:
            if cur == tail:
                return True
            cur = cur.next
            if c%2 == 0:
                tail = tail.next
            c += 1
        return False
