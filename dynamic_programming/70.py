class Solution:
    def climbStairs(self, n: int) -> int:
        # dp -> the ways to the point
        # dp[n] = dp[n-1] + dp[n-2]
        if n < 3:
            return n
        a, b = 1, 2
        for _ in range(2, n):
            c = a + b
            a, b = b, c
        return c
