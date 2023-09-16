class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        return self.dfs(word1, len(word1)-1, word2, len(word2)-1, memo)

    def dfs(self, word1, i, word2, j, memo):
        if i == -1:
            return j+1
        if j == -1:
            return i+1

        if i*9999+j in memo:
            return memo[i*9999+j]

        if word1[i] == word2[j]:
            memo[i*9999+j] = self.dfs(word1, i-1, word2, j-1, memo)
        else:
            ret = min(
                self.dfs(word1, i-1, word2, j, memo),
                self.dfs(word1, i-1, word2, j-1, memo),
                self.dfs(word1, i, word2, j-1, memo)
            )
            ret += 1
            memo[i*9999+j] = ret
        return memo[i*9999+j]