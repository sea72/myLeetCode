from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = 0
        while g and s:
            gg = g[0]
            ss = s[0]
            if gg <= ss:
                content += 1
                g.pop(0)
                s.pop(0)
            else:
                s.pop(0)
        return content

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gg = ss = 0
        while gg < len(g) and ss < len(s):
            if g[gg] <= s[ss]:
                gg += 1
                ss += 1
            else:
                ss += 1
        return gg
            




sol = Solution()
print(sol.findContentChildren(g = [1,2], s = [1,2,3]))