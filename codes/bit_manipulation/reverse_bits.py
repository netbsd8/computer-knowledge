class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            bit = (n >> i) & 1
            ret = ret | bit << (31 - i)

        return ret
        