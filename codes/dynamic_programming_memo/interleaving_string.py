class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        m = set()

        return self.dfs(s1, 0, s2, 0, s3, 0, m)

    def dfs(self, s1, i, s2, j, s3, k, m):
        if i == len(s1):
            return s2[j:] == s3[k:]
        if j == len(s2):
            return s1[i:] == s3[k:]

        key = i * len(s3) + j
        if key in m:
            return False

        if s1[i] == s3[k]:
            if self.dfs(s1, i+1, s2, j, s3, k+1, m):
                return True
        if s2[j] == s3[k]:
            if self.dfs(s1, i, s2, j+1, s3, k+1, m):
                return True
        m.add(key)
        return False