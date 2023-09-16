from typing import List


class Solution:
    # O(n) solution
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        # h <= n, so cut off citation[i] > n
        # count sorting
        counts = [0] * (n+1)
        for i in range(n):
            v = min(n, citations[i])
            counts[v] += 1

        # count papers for each index
        s_counts = [0] * (n+1)
        s_counts[n] = counts[n]
        for i in range(n-1, -1, -1):
            s_counts[i] = s_counts[i+1] + counts[i]

        # find h-index
        for i in range(n, -1, -1):
            if s_counts[i] >= i:
                return i

        return n 

    # # O(nlogn) solution
    # def hIndex(self, citations: List[int]) -> int:
    #    s_citations = sorted(citations, reverse=True)
    #     for i,v in enumerate(s_citations):
    #         if v <= i:
    #             return i
    #     return len(s_citations)

    # O(n^2) solution
    def hIndex_space(self, citations: List[int]) -> int:
        h = 0
        for i in range(len(citations)):
            count = 0
            for j in range(len(citations)):
                if citations[j] >= citations[i]:
                    count += 1
            if count >= citations[i]:
                h = max(h, citations[i])
            else:
                h = max(h, count)

        return h