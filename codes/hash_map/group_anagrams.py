from ast import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for word in strs:
            new_word = "".join(sorted(word))
            if new_word not in m:
                m[new_word] = [word]
            else:
                m[new_word].append(word)

        ret = []
        for v in m.values():
            ret.append(v)

        return ret