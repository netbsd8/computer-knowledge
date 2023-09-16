from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        ret = ListNode()
        cur = ret
        carry = 0
        i, j = 0, 0
        while l1 and l2:
            summ = (carry + l1.val + l2.val) % 10
            carry = (carry + l1.val + l2.val) // 10
            cur.next = ListNode(summ)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            summ = (carry + l1.val) % 10
            carry = (carry + l1.val) // 10
            cur.next = ListNode(summ)
            cur = cur.next
            l1 = l1.next          

        while l2:
            summ = (carry + l2.val) % 10
            carry = (carry + l2.val) // 10
            cur.next = ListNode(summ)
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(1)

        return ret.next  
        