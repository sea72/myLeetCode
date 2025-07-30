from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordLens = [ len(i) for i in wordDict ]
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]

        for j in range(1, len(s)+1):
            for i in range(len(wordDict)):
                if j >= wordLens[i]:
                    for _ in dp[j-wordLens[i]]:
                        if _ + wordDict[i] == s[:j]:
                            dp[j].extend([ _ + wordDict[i]])
        
        return s in dp[len(s)]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i+1):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]

sol = Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))

