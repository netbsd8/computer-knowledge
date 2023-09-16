from typing import List


class Solution_I:
    def singleNumber_I(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret ^= num

        return ret
        
class Solution_II:
    def singleNumber_II(self, nums: List[int]) -> int:
        ret = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1

            count %= 3
            if count:
                ret |= count << i

        if ret >= 2**31:
            ret -= 2**32
        return ret