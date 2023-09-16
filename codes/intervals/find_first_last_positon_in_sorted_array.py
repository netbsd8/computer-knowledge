from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
            
        ret = []
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            ret.append(left)
        elif nums[right] == target:
            ret.append(right)
        else:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            ret.append(right)
        elif nums[left] ==target:
            ret.append(left)

        return ret