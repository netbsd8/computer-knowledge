from ast import List


# sub-matrix: 9x9 -> 3x3 (Valid Sudoku)
for i in range(9):
    for j in range(9):
        k = i // 3
        l = j // 3
        sub_index = k * 3 + l

# get matrix index
class Solution:
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