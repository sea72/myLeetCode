from typing import List
from math import inf
# dp
class Solution0:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[inf for i in range(n)] for j in range(n)]
        mval = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            mval[j][j] = arr[j]
            dp[j][j] = 0
            for i in range(j - 1, -1, -1):
                mval[i][j] = max(arr[i], mval[i + 1][j])
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + mval[i][k] * mval[k + 1][j])
        return dp[0][n - 1]

# decrease stack
class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = []
        for x in arr:
            while stack and stack[-1] <= x:
                y = stack.pop()
                if not stack or stack[-1] > x:
                    res += y * x
                else:
                    res += stack[-1] * y
            stack.append(x)
        while len(stack) >= 2:
            x = stack.pop()
            res += stack[-1] * x
        return res



# greedy 
class Solution:
    def mctFromLeafValues(self, arr:List) -> bool:
        res = 0
        while(len(arr) > 1):
            # 这个题目保证了叶子的顺序，所以不能进行排序,只能找到相邻的最小乘积，并删除其中较小的那个节点
            ma = inf
            idx = -1
            for i in range(0, len(arr)-1 ):
                if (arr[i] * arr[i+1] < ma):
                    ma = arr[i] * arr[i+1]
                    idx = i if arr[i] < arr[i+1] else i+1
            # 更新结果
            res += ma
            # 下一轮
            del arr[idx]
        return res

sol = Solution()
print(sol.mctFromLeafValues([6,5,3,2,4,1,0]))

