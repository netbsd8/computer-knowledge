from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        self.m = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}

        ret = []
        ans = []
        self.dfs(ret, ans, digits)
        return ret

    def dfs(self, ret, ans, digits):
        if digits is None or len(digits) == 0:
            ans_str = "".join(ans)
            ret.append(ans_str)
            return

        for v in self.m[digits[0]]:
            ans.append(v)
            self.dfs(ret,ans, digits[1:])
            ans.pop()
        