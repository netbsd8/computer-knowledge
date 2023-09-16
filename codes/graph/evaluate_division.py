import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = collections.defaultdict(set)

        for equation, value in zip(equations, values):
            x, y = equation[0], equation[1]
            m[x].add((y, value))
            m[y].add((x, 1.0 / value))

        ans = []
        for q in queries:
            visited = set()
            ret = self.dfs(q, m, visited)
            ans.append(ret)

        return ans

    def dfs(self, query, m, visited):
        x = query[0]
        y = query[1]

        if x == y and x in m:
            return 1.0
        if x not in m or y not in m:
            return -1.0

        visited.add(x)
        for neigh, val in m[x]:
            if neigh in visited:
                continue
            new_query = [neigh, y]
            t = self.dfs(new_query, m, visited)
            if t > 0:
                return val * t

        return -1.0