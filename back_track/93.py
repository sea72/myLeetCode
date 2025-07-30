from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        temp = []
        res = []

        def isLegal(str):
            if int(str) < 0 or int(str) > 255:
                return False
            if len(str) > 1 and str[0] == '0':
                return False
            return True

        def dfs(startIdx, dot):
            if startIdx >= n and dot == 4:
                res.append(".".join(temp))
            for end in range(startIdx, n):
                if isLegal(s[startIdx : end+1]):
                    temp.append(s[startIdx : end+1])
                    dfs(end+1, dot+1)
                    temp.pop()

        dfs(0, 0)
        return res

sol = Solution()
print(sol.restoreIpAddresses(s="25525511135"))

