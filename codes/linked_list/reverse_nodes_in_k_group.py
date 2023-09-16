# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 2:
            return head
        next_head = head
        for i in range(k-1):
            next_head = next_head.next
            if next_head is None:
                return head
        ret = next_head
        
        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            tail.next = next_head or current
        return ret