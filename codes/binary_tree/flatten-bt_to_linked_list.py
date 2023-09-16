from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        while root:
            cur = root.left
            while cur and cur.right:
                cur = cur.right

            if cur:
                cur.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
            
    # recursion
    def flatten_recursive(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if root is None:
            return root

        if root.left is None and root.right is None:
            return root

        flat_left = self.helper(root.left)
        flat_right = self.helper(root.right)
        root.right = flat_left
        root.left = None

        cur = root
        while cur and cur.right:
            cur = cur.right
        if cur:
            cur.right = flat_right
        return root