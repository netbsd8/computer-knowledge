class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for v in range(1, n+1):
            while v % 5 == 0:
                count += 1
                v = v // 5

        return count