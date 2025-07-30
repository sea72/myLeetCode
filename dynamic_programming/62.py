class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m+1):
            dp.append([0] * (n+1))
        for x in range(1, m+1):
            for y in range(1, n+1):
                if x == 1 and y == 1:
                    dp[x][y] = 1
                else:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1] 
        return dp[m][n]
    

sol = Solution()
print(sol.uniquePaths(m=3, n=7))

        
