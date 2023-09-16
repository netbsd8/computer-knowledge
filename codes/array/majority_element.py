from typing import List


class Solution:
    # O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        cur = nums[0]
        for num in nums[1:]:
            if num == cur:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    cur = num
                    count = 1

        return cur

    # O(n) space
    def majorityElement_space(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
            if m[num] > len(nums)//2:
                return num

        return -1