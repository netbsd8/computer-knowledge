from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, preSum):
        if root is None:
            return 0

        preSum = preSum * 10 + root.val
        if root.left is None and root.right is None:
            return preSum

        return self.dfs(root.left, preSum) + self.dfs(root.right, preSum)