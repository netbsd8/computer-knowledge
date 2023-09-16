import collections

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # DFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        if Node is None:
            return None

        m = {}
        return self.dfs(node, m)

        # for old_node, new_node in m.items():
        #     for nei in old_node.neighbors:
        #         new_node.neighbors.append(m[nei])

        # return m[node]

    def dfs(self, node, m):
        if node in m:
            return m[node]
        if node is None:
            return None

        new_node = Node(node.val)
        m[node] = new_node

        for nei in node.neighbors:
            new_node.neighbors.append(self.dfs(nei, m))
        return new_node

    # BFS
    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        ret = None
        if node is None:
            return ret

        q = collections.deque()
        # visited = set()
        m = dict()
        q.append(node)

        while q:
            t = q.popleft()
            if t not in m:
                new_node = Node(t.val)
                m[t] = new_node

            for nei in t.neighbors:
                if nei not in m:
                    q.append(nei)

        for old_node, new_node in m.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(m[nei])

        return m[node]