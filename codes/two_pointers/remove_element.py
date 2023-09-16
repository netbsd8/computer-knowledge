from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            while left < len(nums) and nums[left] != val:
                left += 1
            while right >= 0 and nums[right] == val:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # for case "[2] 2"
        if left < len(nums) and nums[left] == val: 
            return left
        if len(nums) == 0:
            return 0

        return left + 1