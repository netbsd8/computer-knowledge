class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        m = dict()

        left, right = 0, 0
        n = len(s)
        ret = 0
        while right < n:
            while right < n and len(m) <= 2:
                if s[right] not in m and len(m) == 2:
                    break
                if s[right] not in m:
                    m[s[right]] = 1
                else:
                    m[s[right]] += 1
                right += 1

            ret = max(ret, right - left)

            m[s[left]] -= 1
            if m[s[left]] == 0:
                m.pop(s[left])
            left += 1

        return ret
