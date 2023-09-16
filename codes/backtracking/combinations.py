from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        ans = []
        self.dfs(ret, ans, k, 1, n)
        return ret

    def dfs(self, ret, ans, k, idx, n):
        if len(ans) == k:
            ret.append(ans.copy())
            return

        for i in range(idx, n+1):
            ans.append(i)
            self.dfs(ret, ans, k, i+1, n)
            ans.pop()
