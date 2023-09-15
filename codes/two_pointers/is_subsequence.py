class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        else:
            if len(t) == 0:
                return False

            if s[0] == t[0]:
                return self.isSubsequence(s[1:], t[1:])
            else:
                return self.isSubsequence(s, t[1:])
        
    def isSubsequence2(self, s: str, t: str) -> bool:
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
                t_i += 1
            else:
                t_i += 1

        if s_i == len(s):
            return True
        return False
