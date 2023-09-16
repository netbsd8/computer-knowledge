import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = collections.defaultdict(list)
        ins = collections.defaultdict(int)
        outs = collections.defaultdict(int)
        
        for course in prerequisites:
            c = course[0]
            p = course[1]
            m[p].append(c)
            ins[c] += 1
            outs[p] += 1

        visited = set()
        q = collections.deque()
        for i in range(numCourses):
            if i not in ins:
                q.append(i)

        if len(q) == 0:
            return False

        while q:
            cur = q.popleft()
            if cur not in visited:
                visited.add(cur)
            else:
                return False

            for nei in m[cur]:
                ins[nei] -= 1
                if ins[nei] == 0:
                    q.append(nei)

        return numCourses == len(visited)