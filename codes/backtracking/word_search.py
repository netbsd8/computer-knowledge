from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, visited, i, j):
                        return True
        return False

    def dfs(self, board, word, visited, i, j):
        if len(word) == 0:
            return True

        m = len(board)
        n = len(board[0])
        if i >= m or i < 0 or j >= n or j < 0:
            return False

        if board[i][j] != word[0]:
            return False

        if visited[i][j]:
            return False

        visited[i][j] = True

        result = False
        result |= self.dfs(board, word[1:], visited, i+1, j)
        result |= self.dfs(board, word[1:], visited, i-1, j)
        result |= self.dfs(board, word[1:], visited, i, j+1)
        result |= self.dfs(board, word[1:], visited, i, j-1)
        
        visited[i][j] = False
        return result