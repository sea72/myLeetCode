from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        profit = 0
        for no in range(len(prices)):
            if prices[no] < buy:
                buy = prices[no]
            if prices[no] > buy:
                profit += prices[no] - buy
                buy = prices[no]

        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return max(dp[-1])


    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
