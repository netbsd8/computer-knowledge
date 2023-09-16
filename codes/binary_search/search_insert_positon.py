from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[right] < target:
            return right + 1
        elif nums[left] >= target:
            return left
        elif nums[right] == target:
            return right

        return right