from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        ans = []
        
        self.dfs(ret, ans, candidates, target, 0)
        return ret

    def dfs(self, ret, ans, candidates, target, idx):
        if sum(ans) > target:
            return

        if sum(ans) == target:
            ret.append(ans.copy())
            return

        for i in range(idx, len(candidates)):
            ans.append(candidates[i])
            self.dfs(ret, ans, candidates, target, i)
            ans.pop()
