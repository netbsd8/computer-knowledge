from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = ""
        if not root:
            return ret

        q = deque()
        q.append(root)

        while q:
            t = q.popleft()
            if not t:
                ret += '$'
                ret += '#'
            else:
                ret += str(t.val)
                ret += '#'
                q.append(t.left)
                q.append(t.right)
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        q = deque()
        pos = data.find('#')
        root = TreeNode(int(data[0:pos]))
        q.append(root)
        data = data[pos+1:]

        while q:
            t = q.popleft()
            pos = data.find('#')
            if data[0:pos] != '$':
                left_node = TreeNode(int(data[0:pos]))
                t.left = left_node
                q.append(left_node)
            data = data[pos+1:] # skip '#'

            pos = data.find('#')
            if data[0:pos] != '$':
                right_node = TreeNode(int(data[0:pos]))
                t.right = right_node
                q.append(right_node)
            data = data[pos+1:]

        return root

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))