from typing import List


class Solution:
    # # O(n) solution
    def candy(self, ratings: List[int]) -> int:
        lefts = [1] * len(ratings)
        rights = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                lefts[i] = lefts[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rights[i] = rights[i+1] + 1

        ret = 0
        for i in range(len(ratings)):
            ret += max(lefts[i], rights[i])

        return ret

    # O(n^2) solution
    def candy_space(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        changed = True
        while changed:
            changed = False
            for i in range(len(ratings)):
                if i-1 >=0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1
                    changed = True

                if i+1 <= len(ratings)-1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
                    changed = True

        return sum(candies)