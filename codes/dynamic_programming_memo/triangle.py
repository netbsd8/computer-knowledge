from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        if m == 0:
            return 0

        dp = [[] for _ in range(m)]
        dp[0].append(triangle[0][0])

        for i in range(1, m):
            dp[i] = [0] * (i+1)
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            # print(dp[i])

        ret = float('inf')
        for v in dp[m-1]:
            ret = min(ret, v)
        return ret 