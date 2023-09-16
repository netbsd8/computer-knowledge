from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        counts = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                counts[i][j] = self.countNeighbors(board, i, j)

        for i in range(m):
            for j in range(n):
                neighbors = counts[i][j]
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 0                    
                else: 
                    if neighbors == 3:
                        board[i][j] = 1

        return

    def countNeighbors(self, board, i, j):
        m = len(board)
        n = len(board[0])

        diffs = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        count = 0
        for diff in diffs:
            x = i + diff[0]
            y = j + diff[1]

            if (x < 0 or x >= m or y < 0 or y >= n):
                continue

            if board[x][y] == 1:
                count += 1

        return count