from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}

        sh = head
        dummy = Node(0)
        cur = dummy
        while head:
            cur.next = Node(head.val)
            m[head] = cur.next
            cur = cur.next
            head = head.next

        head = sh
        while head:
            if head.random:
                m[head].random = m[head.random]
            head = head.next

        return dummy.next

class Solution_recursive:
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)
        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node