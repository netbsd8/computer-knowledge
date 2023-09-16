from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for cur in range(1, amount+1):
            for coin in coins:
                if (cur-coin >= 0 and dp[cur-coin] != float('inf')):
                    dp[cur] = min(dp[cur], dp[cur-coin]+1)

        if dp[amount] != float('inf'):
            return dp[amount]
        return -1
            