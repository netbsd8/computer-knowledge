class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            bit = (n >> i) & 1
            if bit:
                count += 1

        return count