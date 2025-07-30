from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hoding = -prices[0] - fee
        empty = 0
        for i in range(1, len(prices)):
            empty, hoding = max(empty, hoding + prices[i]), max(hoding, empty - prices[i] - fee)

        return empty
    
sol = Solution()
print(sol.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))
