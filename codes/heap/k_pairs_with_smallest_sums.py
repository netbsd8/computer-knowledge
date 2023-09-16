import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)

        ret = []
        visited = set()
        h = [(nums1[0]+nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and h:
            val, (i, j) = heapq.heappop(h)
            ret.append([nums1[i], nums2[j]])

            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(h, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(h, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))

            k -= 1

        return ret

    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     h = []

    #     for i in range(len(nums1)):
    #         for j in range(len(nums2)):
    #             if len(h) < k:
    #                 heapq.heappush(h, [-nums1[i], -nums2[j]])
    #             else:
    #                 cur_sum = -1*(nums1[i] + nums2[j])
    #                 top_sum = h[0][0] + h[0][1]
    #                 if cur_sum >= top_sum:
    #                     heapq.heappop(h)
    #                     heapq.heappush(h, [-nums1[i], -nums2[j]])

    #     ret = []
    #     while h:
    #           ans = [-1*item for item in h[0]]
    #           ret.append(ans)
    #           heapq.heappop(h)

    #     return ret