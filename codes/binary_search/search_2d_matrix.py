from typing import List


class Solution:
    # pure log(mn)
    # non-pure log(mn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m*n-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            val = matrix[mid//n][mid%n]
            if val == target:
                return True
            elif val > target:
                right = mid
            else:
                left = mid

        if matrix[left//n][left%n] == target or matrix[right//n][right%n] ==target:
            return True
        return False
        
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m = len(matrix)
    #     n = len(matrix[0])

    #     i, j = 0, n-1
    #     while i >= 0 and i < m and j >= 0 and j < n:
    #         t = matrix[i][j]
    #         if t == target:
    #             return True
    #         elif t > target:
    #             j -= 1
    #         else:
    #             i += 1


    #     return False