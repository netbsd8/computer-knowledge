from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left


    def next(self) -> int:
        ret = self.st[-1]
        self.st.pop()
        
        cur = ret.right
        while cur:
            self.st.append(cur)
            cur = cur.left 
        
        return ret.val
        
    def hasNext(self) -> bool:
        if not self.st:
            return False
        return True 


# O(n) space
class BSTIterator_space:
    def __init__(self, root: Optional[TreeNode]):
        self.data = []
        self.index = 0
        self.treeToList(root)

    def next(self) -> int:
        ret = self.data[self.index]
        self.index += 1
        return ret
        
    def hasNext(self) -> bool:
        if self.index < len(self.data):
            return True
        return False

    def treeToList(self, root):
        if root is None:
            return
        
        self.treeToList(root.left)
        self.data.append(root.val)
        self.treeToList(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()