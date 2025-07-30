from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastShown = {}
        for pos, char in enumerate(s):
            lastShown[char] = pos
        start, end = -1, 0
        for cur in range(len(s)):
            end = max(lastShown[s[cur]], end)
            if cur == end:
                res.append(end-start)
                start = cur
        
        return res


sol = Solution()
print(sol.partitionLabels("eaaaabaaec"))


 
