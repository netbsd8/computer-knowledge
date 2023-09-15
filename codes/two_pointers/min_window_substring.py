from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        needs = defaultdict(int)
        for char in t:
            needs[char] += 1

        windows = defaultdict(int)
        count = 0
        maxLen = float('inf')
        ret = ""
        while right < len(s):
            if count < len(t):
                if s[right] in needs:
                    windows[s[right]] += 1
                    if windows[s[right]] <= needs[s[right]]:
                        count += 1
                right += 1

            while left < len(s) and count >= len(t):
                diff = (right - 1) - left + 1;
                if maxLen > diff:
                    maxLen = diff
                    ret = s[left:right]
                if s[left] in windows:
                    windows[s[left]] -= 1
                    if windows[s[left]] < needs[s[left]]:
                        count -= 1
                left += 1
        return ret