from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        inserted = False

        while i < len(intervals):
            while i < len(intervals) and intervals[i][1] < newInterval[0]: 
                ret.append(intervals[i])
                i += 1

            while i < len(intervals) and (intervals[i][0] <= newInterval[1]):
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                i += 1

            if not inserted:
                ret.append(newInterval)
                inserted = True

            while i < len(intervals) and intervals[i][0] > newInterval[1]:
                ret.append(intervals[i])
                i += 1

        if not inserted:
            ret.append(newInterval)
        return ret