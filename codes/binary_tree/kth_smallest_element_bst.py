from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Stack
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        count = 0
        cur = root

        while True:
            while cur:
                st.append(cur)
                cur = cur.left

            if st:
                cur = st.pop()
                count += 1
                if count == k:
                    return cur.val
                cur = cur.right

        return -1
                

    # DFS
    def kthSmallest_dfs(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.val = -1

        self.dfs(root, k)
        return self.val

    def dfs(self, root, k):
        if root is None:
            return

        self.dfs(root.left, k)
        if self.count == k:
            self.val = root.val
        self.count += 1
        self.dfs(root.right, k)