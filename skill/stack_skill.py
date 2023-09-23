from typing import Optional

# stack used to loop a bst
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    