from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()

        cur = intervals[0]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if (start <= cur[1]):
                cur[0] = min(cur[0], start)
                cur[1] = max(cur[1], end)
            else:
                ret.append(cur)
                cur = intervals[i]

        ret.append(cur)
        return ret