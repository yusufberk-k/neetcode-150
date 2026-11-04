# Merge Two Sorted Lists
# status: looked | retry: 2026-11-18
# note: retry failed, looked again; dummy head + tail pointer, loop while both lists are non-empty,
# attach the smaller node and advance, then tail.next = list1 or list2 for the leftover;
# compare node values (list1.val), not the nodes themselves. O(n+m) time, O(1) space

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0)
        tail = dum

        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = list2
                tail = list2
                list2 = list2.next
            else: 
                tail.next = list1
                tail = list1
                list1 = list1.next
        tail.next = list1 or list2
        return dum.next
