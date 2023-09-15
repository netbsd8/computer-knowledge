from typing import List


class Solution:
    # O(n) solution
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        min_len = float('inf')

        cur_sum = 0
        left, right = 0, 0

        while right < len(nums):
            while right < len(nums) and cur_sum < target:
                cur_sum += nums[right]
                right += 1

            while cur_sum >= target:
                min_len = min(min_len, right - left)
                cur_sum -= nums[left]
                left += 1

        return min_len
        

    # # O(n^2) solution
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     min_len = float('inf')
    #     if target > sum(nums):
    #         return 0

    #     for i in range(len(nums)):
    #         cur_sum = nums[i]
    #         if cur_sum >= target:
    #             return 1

    #         for j in range(i+1, len(nums)):
    #             cur_sum += nums[j]
    #             if cur_sum >= target:
    #                 min_len = min(min_len, j - i + 1)

    #     return min_len