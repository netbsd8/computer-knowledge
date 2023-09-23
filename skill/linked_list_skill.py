class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DLinkedNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

# define a dummy node, in case the first node is impacted
dummy = ListNode(0, head)

# reverse a list
def reverseList(self, head):
    prev = None
    while head:
        t = head.next
        head.next = prev
        prev = head
        head = t

    return prev