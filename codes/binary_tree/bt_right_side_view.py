import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS, search from right to left and add first right node
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ret = []
        def helper(node, level):
            if level == len(ret):
                ret.append(node.val)

            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return ret

    # BFS
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root is None:
            return ret

        q = collections.deque()
        q.append(root)
        while q:
            count = len(q)
            for i in range(count):
                cur = q[0]
                q.popleft()
                if i == count - 1:
                    ret.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return ret