import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_dc:
    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur =cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        lists_len = len(lists)
        list1 = self.mergeKLists(lists[0:lists_len//2])
        list2 = self.mergeKLists(lists[lists_len//2:])
        return self.merge2Lists(list1, list2)

class Solution_heap:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
# class Solution(object):
#     def mergeKLists(self, lists):
        q, h = len(lists), []
        for i in range(q):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
        
        rhead = rtail = ListNode(0)
        
        while h:
            _, i, n = heapq.heappop(h)
            rtail.next = n
            rtail = rtail.next
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
                
        return rhead.next   