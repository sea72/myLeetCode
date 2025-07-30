from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []

        def dfs(startIdx):
            res.append(temp[:]) 
            for idx in range(startIdx, len(nums)):
                temp.append(nums[idx])
                dfs(idx+1)
                temp.pop()
        
        dfs(0)
        return res
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        ans = []

        def dfs(cur, nums):
            nonlocal temp, ans
            if cur == len(nums):
                ans.append(temp[:])
                return
            temp.append(nums[cur])
            dfs(cur + 1, nums)       
            temp.pop()
            dfs(cur + 1, nums)
              
        dfs(0, nums)
        return ans
    
sol = Solution()
print(sol.subsets([3,4]))

