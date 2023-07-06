from typing import List
import bisect
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubSeq(temp):
            i, j = 0, 0
            while i < len(p) and j < len(temp):
                if p[i] == temp[j]:
                    i += 1
                j += 1
            return i == len(p)
        
        def leftStr(k):
            temp = [1] * len(s)
            for i in range(k):
                temp[removable[i]] = 0
            return "".join([ s[i] for i in range(len(temp)) if temp[i]])

        low , high = 0, len(removable)
        while low < high:
            mid = (low + high) // 2 + 1
            if isSubSeq(leftStr(mid)):
                low = mid
            else:
                high = mid - 1
        return low


sd = Solution()
s = "abcab"
p = "abc"
removable = [0,1,2,3,4]
res = sd.maximumRemovals(s, p, removable)
print(res)
