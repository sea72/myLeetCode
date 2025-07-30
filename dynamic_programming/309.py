from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [ [0, 0, 0 ] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[-1][1], dp[-1][2])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        cold = 0
        sell = 0

        for i in range(1, len(prices)):
            hold, cold, sell = max(hold, sell-prices[i]), hold+prices[i], max(cold, sell)
        
        return max(sell, cold)


sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))
