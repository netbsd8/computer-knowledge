from typing import List


class Solution:
    # O(1) space
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) -1 - k)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    # O(n) space
    def rotate_space(self, nums: List[int], k: int) -> None:
        count = k % len(nums)
        t = nums[len(nums)-count:]
        for i in range(len(nums)-count):
            nums[len(nums)-1-i] = nums[len(nums)-1-count-i]
        for i in range(len(t)):
            nums[i] = t[i]

    # brute force
    def rotate_bf(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k%len(nums)):
            t = nums[-1]
            for j in range(len(nums)-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = t