from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        ans = []
        visited = set()

        self.dfs(ret, ans, nums, visited)
        return ret
        
    def dfs(self, ret, ans, nums, visited):
        if len(ans) == len(nums):
            ret.append(ans.copy())
            return

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            ans.append(nums[i])
            self.dfs(ret, ans, nums, visited)
            ans.pop()
            visited.discard(nums[i])