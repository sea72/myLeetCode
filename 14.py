from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        for i in range(len(strs[0])):
            flag = True
            for j in range(1, len(strs)):
                if i >= len(strs[0]) or i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    flag = False
                    break
            if flag:
                i += 1
            else:
                break
        return strs[0][:i]
        

sd = Solution()
temp = sd.longestCommonPrefix(["flower","flow","flight"]) 
print(temp)