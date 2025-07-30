from typing import List
from math import inf

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [inf] * (n+2)
        for no in range(n):
            if no < 2:
                dp[no] = 0
            dp[no+1] = min(dp[no] + cost[no], dp[no+1])
            dp[no+2] = min(dp[no] + cost[no], dp[no+2])
        return dp[n]  


sol = Solution()
print(sol.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))        

