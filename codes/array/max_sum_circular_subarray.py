from typing import List


class Solution_maxsum:
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

class Solution_Circular:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        cur_max, cur_min = 0,0
        max_sum, min_sum = nums[0], nums[0]

        for num in nums:
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min, 0) + num
            min_sum = min(min_sum, cur_min)

            total_sum += num

        if min_sum == total_sum:
            return max_sum

        return max(max_sum, total_sum - min_sum)