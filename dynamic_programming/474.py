from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # 分别考虑0，1的weights限制
        weightsZero = [ str.count('0') for str in strs]
        weightsOne = [ str.count('1') for str in strs ]

        # 初始成三维数组
        dp = [ [ [0] * (n+1) for _ in range(m+1) ] for str in strs ]

        # 初始化
        # 初始化不能只初始化一个点，而是某个点之后的一个方形面
        for j in range(weightsZero[0], m+1):
            for k in range(weightsOne[0], n+1):
                dp[0][j][k] = 1

        
        for i in range(1, len(strs)):
            for j in range(m+1):
                for k in range(n+1):
                    # 确定j,k与weights的相对大小关系
                    if j >= weightsZero[i] and k >= weightsOne[i]:
                        # max不能少，因为你无法确定哪一条路会有更大的值
                        # 这里是两路并举的，而不是说只能选一路
                        # 上面的j,k比较只是排除了不能走某一条路的情况
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-weightsZero[i]][k-weightsOne[i]] + 1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

        return dp[len(strs)-1][m][n]

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        weightsZero = [ str.count('0') for str in strs]
        weightsOne = [ str.count('1') for str in strs ]

        dp = [ [0] * (n+1) for _ in range(m+1)]

        dp[0][0] = 0

        for i in range(len(strs)):
            for j in range( m, weightsZero[i]-1, -1):
                for k in range( n, weightsOne[i]-1, -1):
                    dp[j][k] = max( dp[j][k], dp[j - weightsZero[i]][k - weightsOne[i]] + 1)

        return dp[m][n]
                    



sol = Solution()
print(sol.findMaxForm(strs = ["11111","100","1101","1101","11000"], m = 5, n = 7))
        