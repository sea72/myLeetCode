from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        profit = 0
        for no in range(len(prices)):
            if prices[no] < buy:
                buy = prices[no]
            if prices[no] - buy > profit:
                profit = prices[no] - buy
        return profit
    

sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))