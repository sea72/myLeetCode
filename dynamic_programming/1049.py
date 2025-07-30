from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = stones_sum // 2
        dp = [ [0] * (target + 1) for _ in range(len(stones))]

        # 不要忘了初始化边界条件
        for j in range(stones[0], target + 1):
            dp[0][j] = stones[0]

        for i in range(1, len(stones)):
            for j in range(target + 1):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - stones[i]] + stones[i])
                else:
                    dp[i][j] = dp[i-1][j]
        
        half = dp[len(stones)-1][target]
        # abs is not necessary
        return stones_sum - 2 * half
        # return abs(stones_sum - 2 * half)

sol = Solution()
print(sol.lastStoneWeightII(stones =[2,7,4,1,8,1]))