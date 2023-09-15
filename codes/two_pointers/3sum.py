from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return ret

    # # using set
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     ret = set()
    #     for i in range(len(nums) - 2):
    #         l, r = i + 1, len(nums) - 1

    #         while l < r:
    #             if nums[i] + nums[l] + nums[r] == 0:
    #                 ret.add((nums[i], nums[l], nums[r]))
    #                 l += 1
    #                 r -= 1
    #             elif nums[i] + nums[l] + nums[r] > 0:
    #                 r -= 1
    #             else:
    #                 l += 1

    #     return [list(item) for item in ret ]