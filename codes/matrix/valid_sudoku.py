from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid row
        for i in range(9):
            m = set()
            for j in range(9):
                c = board[i][j]
                if c in m:
                    return False
                if c != '.':
                    m.add(board[i][j])

        # valid col
        for i in range(9):
            m = set()
            for j in range(9):
                c = board[j][i]
                if c in m:
                    return False
                if c != '.':
                    m.add(c)    

        # valid sub-matrix
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                m = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        c = board[k][l]
                        if c in m:
                            return False
                        if c != '.':
                            m.add(c)


        return True    