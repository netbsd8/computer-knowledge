import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if root is None:
            return ret

        q = collections.deque()
        q.append(root)

        flag = 1
        while q:
            level = []
            count = len(q)
            for i in range(count):
                cur = q.popleft()
                if flag % 2:
                    level.append(cur.val)
                else:
                    level = [cur.val] + level
                if cur.left:
                    q.append(cur.left) 
                if cur.right:
                    q.append(cur.right)
            ret.append(level)
            flag += 1

        return ret