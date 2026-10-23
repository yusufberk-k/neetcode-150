# Merge Two Sorted Lists
# status: hint | retry: 2026-10-31
# note: dummy head node so there is no special case for the first node; walk both lists, attach the
# smaller node to cur.next and step forward; when one list runs out, attach the rest of the other

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        cur1 = list1
        cur2 = list2
        cur = dummy

        while True:
            if cur1 == None:
                cur.next = cur2
                return dummy.next
            elif cur2 == None:
                cur.next = cur1
                return dummy.next
            if cur1.val > cur2.val:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next
            else: 
                cur.next = cur1
                cur = cur1
                cur1 = cur1.next
