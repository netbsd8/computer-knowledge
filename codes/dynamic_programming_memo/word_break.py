from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = set()
        for word in wordDict:
            m.add(word)
        memo = {}

        return self.dfs(s, 0, len(s), memo, m)


    def dfs(self, s, idx, n, memo, m):
        if idx >= n:
            return True
        if s in m:
            return True

        if idx in memo:
            return memo[idx]

        ret = False
        for i in range(idx, n):
            if s[idx:i+1] in m:
                ret |= self.dfs(s, i+1, n, memo, m)
        
        memo[idx] = ret 
        return ret        