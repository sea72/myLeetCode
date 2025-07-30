from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        m =  len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for _ in range(m+1):
            dp.append([0] * (n+1))
        for x in range(1, m+1):
            for y in range(1, n+1):
                if x == 1 and y == 1:
                    dp[x][y] = 1
                else:
                    fromRight = dp[x-1][y] if obstacleGrid[x-1-1][y-1] == 0 else 0
                    fromLeft = dp[x][y-1] if obstacleGrid[x-1][y-1-1] == 0 else 0
                    dp[x][y] = fromLeft + fromRight
        return dp[m][n]
    

sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))