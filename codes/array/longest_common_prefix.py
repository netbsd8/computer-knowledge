from typing import List


class Solution:
    # python style
    def longestCommonPrefix(self, str: List[str]) -> str:
        ret = ""
        for letters in zip(*str):
            if len(set(letters)) == 1:
                ret += letters[0]
            else:
                return ret

        return ret

    # general solution
    def longestCommonPrefix_general(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        count = 0
        cur = strs[0]
        flag = False
        for c in strs[0]:
            for word in strs:
                if count >= len(word):
                    flag = True
                    break
                if word[count] != c:
                    flag = True
                    break
            if flag:
                break
            count += 1 
            
        return strs[0][0:count]
            
    # # longest common prefix for non-all words
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     strs.sort()

    #     m = {}
    #     count = 0
    #     ret = ""
    #     for s in strs:
    #         for i in range(len(s)):
    #             if s[0:i] not in m:
    #                 m[s[0:i]] = 1
    #             else:
    #                 m[s[0:i]] += 1
    #                 if i > count:
    #                     count = i
    #                     ret = s[0:i]

    #     return ret