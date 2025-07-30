from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        
        # return max(sell1, buy2, sell2)
        # sell1 will change to sell2 by default
        # buy2 will not lead to negative
        return sell2

sol = Solution()
print(sol.maxProfit([3,3,5,0,0,3,1,4]))

            
            
            
            

            