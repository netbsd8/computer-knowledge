from typing import List


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict = {}
        wordNum = len(words)
        for i in words:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        wordLen = len(words[0])
        res = []
        
        for i in range(len(s)+1-wordLen*wordNum):
            curr = {}
            j = 0
            while j < wordNum:
                word = s[i+j*wordLen:i+j*wordLen+wordLen]
                if word not in dict:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1
                if curr[word] > dict[word]:
                    break
                j += 1
            if j == wordNum:
                res.append(i)
        return res