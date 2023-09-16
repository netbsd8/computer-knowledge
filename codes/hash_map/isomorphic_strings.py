class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_m = {}
        t_m = set()

        for s_c, t_c in zip(s, t):
            if s_c not in s_m:
                if t_c not in t_m:
                    s_m[s_c] = t_c
                    t_m.add(t_c)
                else:  # eggd --> addd
                    return False
            else:
                if s_m[s_c] != t_c:
                    return False

        return True
