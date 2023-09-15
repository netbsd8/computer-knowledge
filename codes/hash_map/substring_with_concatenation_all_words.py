from typing import List


class Solution:
    # O(n * (a*b)) solution: n as the length of s, a as the length of words, and b as the length of each word
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        m = dict()
        for word in words:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1
        ret = []

        for i in range(0, len(s) - word_len*len(words)+1, 1):
            if self.isMatch(s, i, word_len*len(words), word_len, m):
                ret.append(i)

        return ret
        
    def isMatch(self, s, start, length, word_len, m):
        m2 = m.copy()
        for i in range(start, start+length, word_len):
            word = s[i:i+word_len]
            if word not in m2:
                return False

            m2[word] -= 1
            if m2[word] == 0:
                m2.pop(word)

        if len(m2) == 0:
            return True
        return False