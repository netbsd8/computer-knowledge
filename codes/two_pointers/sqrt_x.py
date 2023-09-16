class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left + 1 < right:
            mid = left + (right - left) // 2
            cur = mid*mid

            if cur == x:
                return mid
            elif cur < x:
                left = mid
            else:
                right = mid

        if right*right <= x:
            return right
        return left