from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n == 0:
            return 1
        if m < n:
            return 0
        dp = [[-1] * 58 for _ in range(m)]
        dp[-1][ ord(s[-1]) - 65 ] = m-1


        for i in range(m-2, -1, -1):
            for j in range(65, 123):
                if chr(j) == s[i]:
                    dp[i][j-65] = i
                else:
                    dp[i][j-65] = dp[i+1][j-65]
        
        @lru_cache(maxsize=None)
        def puzzle(start, remain):
            if remain == 0:
                return 1
            if start >= m:
                return 0
            idx = dp[start][ord(t[n - remain]) - 65]
            if idx == -1:
                return 0
            else:
                return puzzle(idx + 1, remain - 1) + puzzle(idx + 1, remain)
        
        return puzzle(0, n)
    

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # initial value
        for i in range(m+1):
            dp[i][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]

sol = Solution()
print(sol.numDistinct('redae', 'red'))
