from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points.sort()
        count = 0
        overlap = points[0]

        for i in range(1, len(points)):
            if points[i][0] > overlap[1] or points[i][1] < overlap[0]:
                count += 1
                overlap = points[i]
            else:
                overlap[0] = max(points[i][0], overlap[0])
                overlap[1] = min(points[i][1], overlap[1])

        return count+1