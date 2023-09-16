from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        total_nodes = 1
        while cur and cur.next:
            cur = cur.next
            total_nodes += 1
        # in case k == 0        
        if total_nodes <= 1 or k%total_nodes == 0:
            return head
        
        end = cur
        prev = head
        cur = head
        count = 1
        while count <= total_nodes - (k%total_nodes):
            prev = cur
            cur = cur.next
            count += 1

        prev.next = None
        end.next = head
        return cur

    # rotate solution
    def rotateRight_rotate(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        end = None

        total_nodes = 1
        while cur and cur.next:
            cur = cur.next
            total_nodes += 1
        cur.next = head

        count = 0
        prev = cur
        cur = cur
        print(prev.val)
        while count <= total_nodes - (k%total_nodes):
            prev = cur
            cur = cur.next
            count += 1

        prev.next = None
        return cur