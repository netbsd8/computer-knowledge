import collections


class Solution:
    # dict with O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sm = collections.defaultdict(int)
        tm = collections.defaultdict(int)

        for c in s:
            sm[c] += 1
        for c in t:
            tm[c] += 1

        for k, v in sm.items():
            if tm[k] != v:
                return False

        return True



    # sort with O(nlgn)
    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()

        for i in range(len(sl)):
            if sl[i] != tl[i]:
                return False

        return True