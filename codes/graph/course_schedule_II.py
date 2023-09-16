import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outs = {i:[] for i in range(numCourses)}
        ins = [0] * numCourses
        for course in prerequisites:
            c = course[0]
            p = course[1]
            outs[p].append(c)
            ins[c] += 1

        q = collections.deque()
        for i in range(numCourses):
            if ins[i] == 0:
                q.append(i)

        if len(q) == 0:
            return []

        ret = []
        visited = set()
        while q:
            t = q.popleft()
            if t not in visited:
                visited.add(t)
                ret.append(t)
            else:
                return []

            for nei in outs[t]:
                ins[nei] -= 1
                if (ins[nei] == 0):
                    q.append(nei)

        if len(visited) == numCourses:
            return ret
        return []