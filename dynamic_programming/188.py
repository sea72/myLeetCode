from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 剪枝
        k = min(k, len(prices)//2)

        buys = [ -prices[0] ] * (k + 1)
        sells = [0] * (k + 1)

        for i in range(len(prices)):
            for j in range(1, k+1):
                buys[j] = max(buys[j], sells[j-1] - prices[i])
                sells[j] = max(sells[j], buys[j] + prices[i])
        
        return sells[-1]
    

sol = Solution()
print(sol.maxProfit(k = 2, prices = [3,3,5,0,0,3,1,4]))
