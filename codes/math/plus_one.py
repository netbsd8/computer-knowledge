from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        carry = 1
        for d in digits[::-1]:
            s = (d + carry) % 10
            carry = (d + carry) // 10
            ret.insert(0, s)

        if carry:
            ret.insert(0, 1)
        return ret  
        