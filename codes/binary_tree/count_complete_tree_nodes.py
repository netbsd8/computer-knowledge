from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subHight(self, root):
        """
        Return tree depth in O(d) time.
        """
        count = 0
        while root.left:
            root = root.left
            count += 1
        return count

    def isExist(self, idx, d, node):
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx > pivot:
                node = node.right
                left = pivot + 1
            else:
                node = node.left
                right = pivot

        return node is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        d = self.subHight(root)
        if d == 0:
            return 1

        left, right = 0, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.isExist(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return 2**d - 1 + left


    # Not a real < O(n) algorithm
    def countNodes_2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_height = 0
        left_node = root
        while left_node:
            left_height += 1
            left_node = left_node.left

        right_height = 0
        right_node = root
        while right_node:
            right_height += 1
            right_node = right_node.right

        if left_height == right_height:
            return 2**left_height - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)