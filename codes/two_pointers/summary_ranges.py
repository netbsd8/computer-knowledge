from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        i = 0
        while i < len(nums):
            j = i
            k = i
            while k < len(nums):
                if k > j and nums[k-1] + 1 != nums[k]:
                    break
                else:
                    k += 1
                    # i += 1

            ans = str(nums[j])
            if j != k-1:
                ans += "->" + str(nums[k-1])
            ret.append(ans)
            i = k

        return ret
