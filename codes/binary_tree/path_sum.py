from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
            else:
                return False

        new_target = targetSum - root.val
        if self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target):
            return True
        else:
            return False