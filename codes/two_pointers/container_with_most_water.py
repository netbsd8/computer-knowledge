from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            curArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, curArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

    # # O(n^2) solution
    # def maxArea(self, height: List[int]) -> int:
    #     maxArea = 0
    #     for i in range(0, len(height)):
    #         for j in range(i+1, len(height)):
    #             maxArea = max(maxArea, min(height[i], height[j]) * (j - i))

    #     return maxArea