from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in coins:
            for j in range(i, amount + 1):
                if dp[j-i] > -1 and dp[j] > -1:
                    dp[j] = min(dp[j-i]+1, dp[j])
                elif dp[j] == -1 and dp[j-i] > -1:
                    dp[j] = dp[j-i] + 1
        return dp[amount]

import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ math.inf ] * (amount + 1)
        dp[0] = 0

        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j-i]+1, dp[j])

        return dp[amount] if dp[amount] != math.inf else -1
    

sol = Solution()
print(sol.coinChange([1,2,5],  11))