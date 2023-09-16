class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        patterns = list(pattern)

        m = {}
        used = set()

        for word, p in zip(words, pattern):
            if word not in m:
                if p not in used:
                    m[word] = p
                    used.add(p)
                else:
                    return False
            else:
                if m[word] != p:
                    return False

        return True