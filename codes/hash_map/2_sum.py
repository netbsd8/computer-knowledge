from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        m = {}

        for i, num in enumerate(nums):
            if target - num in m:
                ret.append(m[target - num])
                ret.append(i)
                return ret
            else:
                m[num] = i

        return ret