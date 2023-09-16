import collections


class Solution:
    # one map
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = collections.Counter(magazine)

        for c in ransomNote:
            if c not in m or m[c] <= 0:
                return False

            m[c] -= 1

        return True

    # two maps
    def canConstruct_2maps(self, ransomNote: str, magazine: str) -> bool:
        r_m = collections.defaultdict(int)
        m_m = collections.defaultdict(int)

        for c in ransomNote:
            r_m[c] += 1

        for c in magazine:
            m_m[c] += 1

        for c in ransomNote:
            if r_m[c] > m_m[c]:
                return False

        return True