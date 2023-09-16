from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root)

    def getMaxDepth(self, root):
        if not root:
            return 0
        leftDepth = self.getMaxDepth(root.left)
        rightDepth = self.getMaxDepth(root.right)
        return 1 + max(leftDepth, rightDepth)