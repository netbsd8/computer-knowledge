from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        ans = []

        self.dfs(ret, ans, n, 0, 0)
        return ret

    def dfs(self, ret, ans, n, left_count, right_count):
        if len(ans) == n * 2:
            ans_str = "".join(ans)
            ret.append(ans_str)
            return

        if left_count < n:
            ans.append('(')
            self.dfs(ret, ans, n, left_count+1, right_count)
            ans.pop()

        if right_count < left_count:
            ans.append(')')
            self.dfs(ret, ans, n, left_count, right_count + 1)
            ans.pop()