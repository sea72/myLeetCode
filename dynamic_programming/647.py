class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for n in range(2 * len(s) + 1):
            left = n // 2
            right = left + (n % 2)
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

class Solution: 
    def countSubstrings(self, s: str) -> int:
        res = 0
        s = "#".join(s)
        s = "$#" + s + "#!"
        n = len(s)
        dp = [0] * n
        l, r = 0, -1
        for i in range(0, n):
            k = 1 if i > r else min(dp[l + r - i], r - i + 1)
            # k没有减1，所以 i+k 和 i-k都是待验证的，未对比的字符
            # 如果相等那么半径加1
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            dp[i] = k
            res += k // 2
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k
        return res


class Solution: 
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i == j or j == i + 1:
                        dp[i][j] = True
                        res += 1
                    elif dp[i+1][j-1]:

                        dp[i][j] = True
                        res += 1
                else:
                    pass
        return res

sol = Solution()
print(sol.countSubstrings('aaa'))
