from typing import List


class Solution_1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)

        if l % 2:
            return self.findKth(nums1, nums2, l//2)
        else:
            return (self.findKth(nums1, nums2, l//2-1) + self.findKth(nums1, nums2, l//2)) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return nums2[k]

        if len(nums1) + len(nums2) - 1 == k:
            return max(nums1[-1], nums2[-1])

        i = len(nums1) // 2
        j = k - i
        if nums1[i] > nums2[j]:
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)

class Solution_2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)

        if l % 2:
            return self.findKth(nums1, nums2, 0, 0, l//2 + 1)
        else:
            return (self.findKth(nums1, nums2, 0, 0, l//2) + self.findKth(nums1, nums2, 0, 0, l//2 + 1)) / 2

    def findKth(self, nums1, nums2, i, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])

        if i + k//2 - 1 < len(nums1):
            mid1 = nums1[i + k//2 - 1]
        else:
            mid1 = float('inf')

        if j + k//2 - 1 < len(nums2):
            mid2 = nums2[j + k//2 - 1]
        else:
            mid2 = float('inf')

        if mid1 < mid2:
            return self.findKth(nums1, nums2, i + k//2, j, k - k//2)
        else:
            return self.findKth(nums1, nums2, i, j + k//2, k - k//2)