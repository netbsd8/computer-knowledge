from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        left, right = 0, 1
        count = 1

        while right < len(nums):
            if nums[left] != nums[right]:
                count = 1
                left += 1
                nums[left] = nums[right]
                right += 1
            else:
                count += 1
                if count > 2:
                    right += 1
                else:
                    left += 1
                    nums[left] = nums[right]
                    right += 1

        return left+1


    # using extra spaces
    def removeDuplicates_space(self, nums: List[int]) -> int:
        s_list = []
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1

        for num in nums:
            for i in range(min(2, m[num])):
                s_list.append(num)
            m[num] = 0

        for i in range(len(s_list)):
            nums[i] = s_list[i]

        return len(s_list)