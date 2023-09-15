from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0

        while right < len(chars):
            # right: count
            cur = chars[right]
            cnt = 0
            while right < len(chars) and cur == chars[right]:
                right += 1
                cnt += 1

            # left: update the pattern
            chars[left] = cur
            if cnt == 1:
                left += 1
            else:
                left += 1
                cnt_str = str(cnt)
                for i in range(len(cnt_str)):
                    chars[left] = cnt_str[i]
                    left += 1

        return left
        