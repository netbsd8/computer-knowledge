import collections
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = collections.deque()
        visited = set()
        q.append(startGene)

        count = 0
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if t == endGene:
                    return count
                if t not in visited:
                    visited.add(t)

                for i in range(len(t)):
                    for c in ['A', 'C', 'G', 'T']:
                        new_t = t[0:i] + c + t[i+1:]
                        if new_t in visited:
                            continue
                        if new_t not in bank:
                            continue
                        q.append(new_t)
            count += 1

        return -1