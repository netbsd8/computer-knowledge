from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        lefts = [0] * len(height)
        rights = [0] * len(height)

        max_left = height[0]
        for i in range(1, len(height)):
            lefts[i] = max_left
            max_left = max(max_left, height[i])

        max_right = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            rights[i] = max_right
            max_right = max(max_right, height[i])

        ret = 0
        for i in range(len(height)):
            min_height = min(lefts[i], rights[i])
            if height[i] < min_height:
                ret += min_height - height[i]

        return ret 