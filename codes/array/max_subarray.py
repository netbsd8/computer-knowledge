from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = float('-inf')
        ret = nums[0]

        for i, v in enumerate(nums):
            if cur_sum <= 0:
                cur_sum = v
            else:
                cur_sum += v
            ret = max(ret, cur_sum)

        return ret