from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        fast, slow = head, head
        prev = dummy
        count = 1
        while count < n and fast:
            fast = fast.next
            count += 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next

        return dummy.next