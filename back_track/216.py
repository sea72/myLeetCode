from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        temp = []
        
        def combine(start, remain):
            if remain < 0:
                return 
            if sum(temp) == n and remain == 0:
                res.append(temp[:])
            for i in range(start, 10):
                temp.append(i)
                combine(i+1, remain-1)
                temp.pop()
        combine(1, k)
        return res
    
sol = Solution()
print(sol.combinationSum3(3, 9))
        