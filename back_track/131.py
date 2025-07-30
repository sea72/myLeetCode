from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        temp = []
        res = []

        isRecurve = [ [True] * n for _ in range(n) ]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                isRecurve[i][j] = isRecurve[i+1][j-1] and (s[i] == s[j])
        

        def dfs(startIdx):
            if startIdx == n:
                res.append(temp[:])
            
            for pos in range(startIdx, n):
                tempStr = s[startIdx:pos+1]
                if isRecurve[startIdx][pos]:
                    temp.append(tempStr)
                    dfs(pos+1)
                    temp.pop()
        
        dfs(0)
        return res


# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         f = [[True] * n for _ in range(n)]

#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 f[i][j] =  (s[i] == s[j]) and f[i + 1][j - 1]

#         ret = list()
#         ans = list()

#         def dfs(i: int):
#             if i == n:
#                 ret.append(ans[:])
#                 return
            
#             for j in range(i, n):
#                 if f[i][j]:
#                     ans.append(s[i:j+1])
#                     dfs(j + 1)
#                     ans.pop()

#         dfs(0)
#         return ret
        

sol = Solution()
print(sol.partition('aabab'))