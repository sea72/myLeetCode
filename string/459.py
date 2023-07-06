class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pmt = [0]
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = pmt[j-1]
            if s[j] == s[i]:
                j += 1
            pmt.append(j)
        return pmt[-1] != 0 and len(s) % (len(s) - pmt[-1]) == 0

sol = Solution()
print(sol.repeatedSubstringPattern("asdfasdfasdf"))