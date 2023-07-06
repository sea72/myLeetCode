class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen = len(s)
        pLen = len(p)

        # 建立dp
        dp = [[False] * (pLen +1) for _ in range(sLen + 1)]

        # 初始化边界条件
        dp[0][0] = True
        for j in range(2, pLen + 1 ):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        # 开始状态转移，从小往大转
        for i in range(1, sLen +1):
            for j in range(1, pLen +1):
                if p[j-1] in {s[i-1], "."}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if p[j-2] in {s[i-1], "."}:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[sLen][pLen]



sd = Solution()
print(sd.isMatch("aa", "a"))


        
