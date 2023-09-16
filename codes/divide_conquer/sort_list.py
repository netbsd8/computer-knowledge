from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head1 = head
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = None
        p1 = self.sortList(head1)
        p2 = self.sortList(slow)
        return self.mergeLists(p1, p2)
        
    
    def mergeLists(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1:
            cur.next = head1
        if head2:
            cur.next = head2

        return dummy.next;