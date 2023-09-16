from typing import List

# I
class Solution_I:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        return False

   # DP O(N^2) solution
    def canJump_dp(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(len(nums)):
            if i != 0 and dp[i] == 0:
                return False
            for j in range(i+1, i+1+nums[i]):
                dp[j] = 1
                if dp[len(nums)-1] == 1:
                    return True

        return True 


# II  
class Solution_II:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        i = 0
        cur_max = 0
        last_max = 0

        while i < len(nums)-1:
            last_max = cur_max
            while i <= last_max:
                cur_max = max(cur_max, i+nums[i])
                if i + nums[i] >= len(nums)-1:
                    return jumps + 1
                i += 1
            jumps += 1

        return jumps