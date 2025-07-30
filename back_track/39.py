from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backTrace(curr):
            s = sum(temp)
            if s > target:
                return 
            elif s == target:
                res.append(temp[:])
                return 
            for index in range(curr, len(candidates)):
                temp.append(candidates[index])
                backTrace(index)
                temp.pop()
        
        backTrace(0)
        return res

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
            
