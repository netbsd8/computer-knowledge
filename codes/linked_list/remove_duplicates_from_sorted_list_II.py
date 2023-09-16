import collections
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # directly remove
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        prev = dummy

        while cur:
            start = cur
            count = 0
            while cur and cur.val == start.val:
                cur = cur.next
                count += 1
            if count == 1:
                prev.next = start
                prev = prev.next
        
        prev.next = None

        return dummy.next

         
    # using map to count
    def deleteDuplicates_map(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = collections.defaultdict(int)

        cur = head
        while cur:
            m[cur.val] += 1
            cur = cur.next

        dummy = ListNode(0, head)
        cur = dummy

        while head:
            if m[head.val] == 1:
                cur.next = head
                cur = cur.next
            head = head.next

        cur.next = None
        return dummy.next