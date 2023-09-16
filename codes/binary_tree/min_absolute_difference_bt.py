from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.diff = float('inf')
        self.prev = None
        prev = [None]
        self.dfs(root)

        return self.diff

    def dfs(self, root):
        if root.left:
            self.dfs(root.left);
        if self.prev:
            self.diff = min(self.diff, abs(root.val - self.prev.val))
        self.prev = root
        if root.right:
            self.dfs(root.right);

    # # DFS with a list
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:    
    #     data = []
    #     self.dfs(root, data)

    #     ret = float('inf')
    #     for i in range(1, len(data)):
    #         ret = min(ret, abs(data[i] - data[i-1]))

    #     return ret

    # def dfs(self, root, data):
    #     if root is None:
    #         return

    #     self.dfs(root.left, data)
    #     data.append(root.val)
    #     self.dfs(root.right, data)
        
    # # DFS without list
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     self.minDistance = 1e9
    #     # Initially, it will be null.
    #     self.prevNode = None

    #     def inorder(node):
    #         if node is None:
    #             return
    #         inorder(node.left)
    #         # Find the difference with the previous value if it is there.
    #         if self.prevNode is not None:
    #             self.minDistance = min(self.minDistance, node.val - self.prevNode)
    #         self.prevNode = node.val
    #         inorder(node.right)

    #     inorder(root)
    #     return self.minDistance
