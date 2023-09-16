from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        # find left
        prev = dummy
        cur = head
        count = 1
        while cur and count < left:
            cur = cur.next
            prev = prev.next
            count += 1

        left_head = cur
        while cur and count < right:
            cur =cur.next
            count += 1
        right_next = cur.next
        cur.next = None
        prev.next = self.reverseList(left_head)
        left_head.next = right_next

        return dummy.next       


    def reverseList(self, head):
        prev = None
        while head:
            t = head.next
            head.next = prev
            prev = head
            head = t

        return prev