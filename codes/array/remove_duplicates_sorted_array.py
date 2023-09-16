from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1

            if right < len(nums):
                left += 1
                nums[left] = nums[right]
                right += 1
            
        return left + 1
        