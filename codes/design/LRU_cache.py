class DLinkedNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = dict()
        self.head = DLinkedNode(-1, -1)
        self.tail = DLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        # print("Get Operating: ", key)
        if key not in self.m:
            return -1

        node = self.m[key]
        self.remove(node)
        self.push_front(node)
        # print(self.m)
        # self.printList()

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # print("Put Operating: ", key)
        if key in self.m:
            node = self.m[key]
            node.val = value
            self.remove(node)
            self.push_front(node)
        else:
            node = DLinkedNode(key, value)
            if len(self.m) < self.capacity:
                self.push_front(node)
            else:
                del_node = self.tail.prev
                # print("Deleting", del_node.val)
                del_key = del_node.key
                self.remove(del_node)
                self.push_front(node)
                del self.m[del_key]


            self.m[key] = node
        # print(self.m)
        # self.printList()
    
    def push_front(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node


    def remove(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def printList(self):
        ls = []
        cur = self.head
        while cur != self.tail:
            ls.append(cur.val)
            cur = cur.next
        ls.append(cur.val)
        print(ls)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)