import heapq
from typing import List


class Solution:
    # quick sorting solution
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, k, 0, len(nums)-1)

    def quickSelect(self, nums, k, start, end):
        l, r = start, end
        mid = l + (r-l)//2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if start + k -1 <= r:
            return self.quickSelect(nums, k, start, r)
        if start + k - 1 >= l:
            return self.quickSelect(nums, k-(l-start), l, end)
        return nums[r+1]

    # heap solution
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        h = []

        for i in range(k):
            heapq.heappush(h, nums[i])

        for num in nums[k:]:
            if num > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, num)

        return h[0]