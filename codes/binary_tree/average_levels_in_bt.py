import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        levels = []
        if root is None:
            return ret

        self.helper(0, root, levels)
        for level in levels:
            cur = 0
            for val in level:
                cur += val
            ret.append(cur/len(level))
        
        return ret

    def helper(self, level, node, levels):
        if node is None:
            return

        if level >= len(levels):
            levels.append([])
        levels[level].append(node.val)
        
        self.helper(level+1, node.left, levels)
        self.helper(level+1, node.right, levels)

    # BFS
    def averageOfLevels_bfs(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        if root is None:
            return ret

        q = collections.deque()
        q.append(root)

        while q:
            ans = 0
            count = len(q)
            for i in range(count):
                cur = q.popleft()
                ans += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ret.append(ans/count)

        return ret