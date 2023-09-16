# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.left is None and root.right is None:
            if root == p or root == q:
                return root
            else:
                return None

        if root == p or root == q:
            return root
        else:
            l_ret = self.lowestCommonAncestor(root.left, p, q)
            r_ret = self.lowestCommonAncestor(root.right, p, q)
            if l_ret != None and r_ret != None:
                return root
            elif l_ret == None:
                return r_ret
            else:
                return l_ret