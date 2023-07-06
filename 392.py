# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(t) < len(s):
#             return False
#         i, j = 0, 0
#         while i < len(s):
#             if s[i] == t[j]:
#                 i += 1
#             if j < len(t) - 1:
#                 j += 1
#             else:
#                 break
#         return True if i == len(s) else False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         sLen, tLen = len(s), len(t)
#         if tLen == 0 and sLen == 0:
#             return True
#         if tLen < sLen:
#             return False
#         firstShow = [[ None ] * 26 for _ in range( tLen )]
#         for j in range(26):
#             firstShow[tLen-1][j] = tLen - 1 if t[-1] == chr(j + 97) else None
#         for i in range( tLen-2, -1, -1):
#             for j in range(26):
#                 if t[i] == chr( j + 97):
#                     firstShow[i][j] = i
#                 else:
#                     firstShow[i][j] = firstShow[i+1][j]
#         i, j = 0, 0
#         while j < sLen and i < tLen:
#             if firstShow[i][ord(s[j]) - 97] is None or firstShow[i][ord(s[j]) - 97] > tLen - 1:
#                 return False
#             else:
#                 i = firstShow[i][ord(s[j]) - 97] + 1
#                 j += 1
#         if j == sLen:
#             return True
#         else:
#             return False

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        
        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        
        return True




sd = Solution()
s = ""
t = ""
res = sd.isSubsequence(s, t)
print(res)
