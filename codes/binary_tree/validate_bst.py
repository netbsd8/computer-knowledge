from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # dfs
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev_val = float('-inf')
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return True
        
        if self.dfs(root.left) == False:
            return False
        if self.prev_val >= root.val:
            return False
        self.prev_val = root.val
        return self.dfs(root.right)

        

class Solution_2:
    # stack
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = []
        cur = root
        prev = None

        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left

            # if st:
            cur = st.pop()
            if prev:
                if prev.val >= cur.val:
                    return False
            prev = cur
            cur = cur.right

        return True