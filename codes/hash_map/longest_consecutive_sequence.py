from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)

        max_count = 0
        while m:
            val = m.pop()
            cur_count = 1
            next_val = val + 1
            prev_val = val - 1
            while True:
                if next_val not in m and prev_val not in m:
                    max_count = max(max_count, cur_count)
                    cur_count = 0
                    break
                else:
                    if next_val in m:
                        cur_count += 1
                        m.discard(next_val)
                        next_val += 1
                    if prev_val in m:
                        cur_count += 1
                        m.discard(prev_val)
                        prev_val -= 1

        return max_count

    # # memory exhausted
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)

    #     max_val, min_val = max(nums), min(nums)
    #     data = [False for _ in range(min_val, max_val+1)]

    #     for num in nums:
    #         i = num - min_val
    #         data[i] = True

    #     count = 0
    #     ret = 0
    #     for i,v in enumerate(data):
    #         if v == False:
    #             ret = max(ret, count)
    #             count = 0
    #         else:
    #             count += 1

    #     return max(ret, count) # in case, the whole array is a consecutive sequence
        