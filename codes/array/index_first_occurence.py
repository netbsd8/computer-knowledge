class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            h_index = i
            found = True
            for j in range(len(needle)):
                if h_index >= len(haystack):
                    return -1
                if needle[j] != haystack[h_index]:
                    found = False
                    break;
                h_index += 1

            if found == True:
                return i

        return -1
        