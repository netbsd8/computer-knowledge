from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        count = len(matrix) * len(matrix[0])
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right or top <= bottom:
            # Top left -> right
            for i in range(left, right+1, 1):
                if count == 0:
                    return ret
                ret.append(matrix[top][i])
                count -= 1
            top += 1
            # print(count, ret)
                
            # Right top -> bottom
            for i in range(top, bottom+1, 1):
                if count == 0:
                    return ret
                ret.append(matrix[i][right])
                count -= 1
            right -= 1

            # Bottom right -> left
            for i in range(right, left-1, -1):
                if count == 0:
                    return ret
                ret.append(matrix[bottom][i])
                count -= 1
            bottom -= 1

            # Left bottom -> top
            for i in range(bottom, top-1, -1):
                if count == 0:
                    return ret
                ret.append(matrix[i][left])
                count -= 1
            left += 1

        return ret