from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur = head
        prev = dummy
        greater = ListNode() # greater/equal list
        sec_head = greater
        # smaller list
        while cur:
            if cur.val < x:
                prev.next = cur
                prev = prev.next
            else: 
                greater.next = cur
                greater = greater.next

            cur = cur.next

        # link to greater/equal list
        prev.next = sec_head.next
        if greater:
            greater.next = None

        return dummy.next