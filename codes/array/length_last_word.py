class Solution:
    # python style
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

    # count back to front
    def lengthOfLastWord_2(self, s: str) -> int:
        start = len(s) - 1
        i = start
        while i >= 0:
            if s[i] == ' ':
                start -= 1
                i -= 1
            else:
                break
            

        while i >= 0:
            if s[i] == ' ':
                break
            i -= 1

        return start - i