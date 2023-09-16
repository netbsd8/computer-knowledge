from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for j in range(0, n//2+1):
            # n-1 is needed to make the top right corner item be used
            for i in range(j, n-1-j):
                t = matrix[j][i]
                print(t)
                matrix[j][i] = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
                matrix[i][n-1-j] = t
                print(matrix)

        return