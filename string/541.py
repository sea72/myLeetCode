class Solution0:
    def reverseStr(self, s: str, k: int) -> str:
        newS = ""
        while len(s) >= 2 * k:
            newS += s[k-1::-1] + s[k: 2*k]
            s = s[2 * k:]
        if len(s) >= k:
            newS += s[k-1::-1] + s[k:]
        else:
            newS += s[::-1]
        return newS

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)


sol = Solution()
print(sol.reverseStr("abc", 4))