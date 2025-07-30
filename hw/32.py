def solve():
    '''
    求的是最大公共子串，但其并不一定是正确的回文子串
    如 aacbzcaa 中的aac，反过来是caa ,但并不是正确答案
    '''

    string = input()
    stringR = string[::-1]
    n = len(string)
    dp = [ [0] * n for _ in range(n)  ]
    maxLen = 0

    for i in range(n):
        if string[i] == stringR[-1]:
            dp[i][n-1] = 1

    for j in range(n):
        if stringR[j] == string[-1]:
            dp[n-1][j] = 1


    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if string[i] == stringR[j] else 0
                maxLen = max(maxLen, dp[i][j])

    print(maxLen)



def longestPalindrome():
    s = input()
    maxLen = 0
    if len(s) == 1:
        return s
    else:
        for i in range(len(s)):
            for j in range(len(s)-1, -1, -1):
                if j-i+1 <= maxLen:
                    break
                elif s[i:j+1] == s[j:i-1:-1]:
                    maxLen = j-i+1
                    break
        return maxLen


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#".join('^' + s + '$')
        curCenter = 0
        rightMost = 0
        arm = [ 0 ] * len(s)
        armMax = 0
        centerMax = 0

        for i in range(1, len(s)-1):
            if i <= rightMost:
                arm[i] = min( rightMost - i, arm[2*curCenter-i])
            # expand
            while s[i + arm[i] + 1] == s[i - arm[i] - 1]:
                arm[i] += 1
            if i + arm[i] > rightMost:
                rightMost = i + arm[i]
                curCenter = i
            if arm[i] > armMax:
                armMax = arm[i]
                centerMax = i
        
        return s[centerMax - armMax + 1: centerMax + armMax:2]

sol = Solution()
print(sol.longestPalindrome('aa'))