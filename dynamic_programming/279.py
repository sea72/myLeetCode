import math

class Solution:
    def numSquares(self, n: int) -> int:
        coins = (i * i for i in range(1, 10**2+1))
        dp = [ math.inf ] * (n + 1)
        dp[0] = 0
        
        for i in coins:
            if i > n:
                break
            for j in range(i, n+1):
                dp[j] = min(dp[j-i] + 1, dp[j])
        return dp[n]


sol = Solution()
print(sol.numSquares(12))