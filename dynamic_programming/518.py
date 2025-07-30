from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[ 0 ] * (amount + 1) for _ in coins]
        for i in range(len(coins)):
            dp[i][0] = 1

        for j in range(coins[0], amount+1):
            dp[0][j] += dp[0][j-coins[0]]

        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[i][j] = dp[i][j - coins[i]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(coins) - 1][amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                    dp[j] += dp[j - coins[i]] 

        return dp[amount]       


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = dp[j] + dp[j-coins[i]]

        return dp[amount]




sol = Solution()
print(sol.change(amount = 5, coins = [1, 2, 5]))