from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        diff = nums[-1] - nums[0] + 1
        miss = diff - len(nums)
        if miss < k:
            return nums[-1] + (k - miss)

        while left + 1 < right:
            mid = left + (right-left)//2
            cur = nums[mid] - nums[left] + 1
            dif = cur - (mid - left + 1)
            if dif >= k:
                right = mid
            elif dif < k:
                k -= dif
                left = mid

        return nums[left] + k