class Solution_dp:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]

class Solution:
    # O(n^2)
    def longestPalindrome(self, s: str) -> str:
        ret = ""

        for i in range(len(s)):
            cur = self.findPalindrome(s, i, i)
            if len(cur) > len(ret):
                ret = cur
            cur = self.findPalindrome(s, i, i+1)
            if len(cur) > len(ret):
                ret = cur

        return ret

    def findPalindrome(self, s, left, right):
        # if s[left] != s[right]:
        #     return s[left]

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]

    # # O(n^3)
    # def longestPalindrome(self, s: str) -> str:
    #     ret = ""
    #     if len(s) == 0:
    #         return ret

    #     ret = s[0]
    #     for i in range(len(s)):
    #         for j in range(i+1, len(s)):
    #             if self.isPalindrom(s, i, j):
    #                 cur = s[i:j+1]
    #                 if len(cur) > len(ret):
    #                     ret = cur

    #     return ret

    # def isPalindrom(self, s, left, right):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True