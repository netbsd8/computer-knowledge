from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        root_pos = inorder.index(postorder[-1])
        root = TreeNode(postorder[-1])
        root.left = self.buildTree(inorder[:root_pos], postorder[:root_pos])
        root.right = self.buildTree(inorder[root_pos+1:], postorder[root_pos:-1])
        return root