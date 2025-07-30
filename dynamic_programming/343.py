import math

class Solution:
    def integerBreak(self, n: int) -> int:
        start = 2
        end = n
        res = 0
        for i in range(start, end + 1):
            decimal = n // i
            more = n - (i - 1) * decimal

            deciaml2 = math.ceil( n / i)
            less = n - (i - 1) * deciaml2

            temp = max(decimal ** (i - 1) * more, deciaml2 ** (i-1) * less)
            if temp > res:
                res = temp
            else:
                break 
        return res
    
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        
        return dp[n]

sol = Solution()
print(sol.integerBreak(16))

