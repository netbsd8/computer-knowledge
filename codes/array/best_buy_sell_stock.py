from typing import List

# I
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        cur_min = prices[0]

        for price in prices[1:]:
            ret = max(ret, price - cur_min)
            cur_min = min(cur_min, price)

        return ret
        
# II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_price = prices[0]

        for price in prices[1:]:
            if price > prev_price:
                profit += price - prev_price
            prev_price = price

        return profit