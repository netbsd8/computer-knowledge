from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                left = mid
            elif nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid

        if nums[left] > nums[right]:
            return left
        return right