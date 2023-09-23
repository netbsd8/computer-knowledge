import collections
import heapq

# init an 2-d array
m = 9
n = 9
visited = [[False] * n for _ in range(m)]

# list
l = [1,2,3,4,5]
# 5
l[-1]
# [5, 4, 3, 2, 1]
l[::-1]
# [1, 2, 3, 4]
l[:-1]

## list copy
l = [1, 2 ,3]
ll = l.copy() # new list, otherwise, ll and l share the same memory range
## index
l.index(2)

# algorithm
a = 5
a.isdigit()

## join
st = []
for cc in list(str(123)):
    st.append(cc)
ret = int(''.join(st))

# Data structure
## hashmap
m = collections.defaultdict(int)
m["1"] = 1
m["2"] = 2
if "1" in m:
    m.pop("1")
del m["2"]

## hashset
s = set()
s.add('a')
s.add('b')
s.add('c')
if 'a' in s:
    s.remove('a')
    s.discard('b')
    s.pop() # no args

## queue
q = collections.deque()
q.append('1')
v = q.popleft()

## priority queue
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        pq = []

        for i in range(len(lists)):
            if lists[i]:
                cur = lists[i]
                heapq.heappush(pq, (cur.val, cur))

        dummy = ListNode(None)
        cur = dummy
        while pq:
            _, min_node = heapq.heappop(pq)[1:]
            cur.next = min_node
            if min_node.next:
                heapq.heappush(pq, (min_node.val, min_node))
            cur = cur.next

        return dummy.next
