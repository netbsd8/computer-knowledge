import collections

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # O(1) space
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        cur = root
        while cur:
            next_level_first = None
            prev = None
            while cur:
                if not next_level_first:
                    next_level_first = cur.left if cur.left \
                                     else cur.right
                if cur.left:
                    if prev:
                        prev.next = cur.left
                        prev = prev.next
                    else:
                        prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                        prev = prev.next
                    else:
                        prev = cur.right

                cur = cur.next

            cur = next_level_first

        return root

    # O(n) space
    def connect_space(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        q = collections.deque()
        q.append(root)
        prev = None

        while q:
            for i in range(len(q)):
                if i == 0:
                    prev = q.popleft()
                    if prev.left:
                        q.append(prev.left)
                    if prev.right:
                        q.append(prev.right)
                else:
                    cur = q.popleft()
                    prev.next = cur
                    prev = prev.next
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                        
        return root