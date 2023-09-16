from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1] * len(nums)
        right_prods = [1] * len(nums)

        for i in range(1, len(nums)):
            left_prods[i] = left_prods[i-1] * nums[i-1]

        for i in range(len(nums)-1-1, -1, -1):
            right_prods[i] =  right_prods[i+1] * nums[i+1]

        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = left_prods[i] * right_prods[i]

        return ret