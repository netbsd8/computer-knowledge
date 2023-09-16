from typing import List


class Solution:
    # O(n) solution
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        if sum(gas) < sum(cost):
            return -1

        ret = 0
        left = 0
        for i in range(len(gas)):
            left = left + gas[i] - cost[i]
            if left < 0:
                left = 0
                ret = i + 1

        return ret

    # O(n^2) solution
    def canCompleteCircuit_space(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            cur_gas = 0
            j = 0
            while j < len(gas):
                p = (i + j) % len(gas)
                cur_gas = cur_gas + gas[p] - cost[p]
                if cur_gas < 0:
                    break
                j += 1

            if j >= len(gas):
                return i
        return -1