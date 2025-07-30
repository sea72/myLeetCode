from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []

        nums.sort()

        def dfs(idx):
            if idx >= len(nums):
                res.append(temp[:])
            else:
                temp.append(nums[idx])
                dfs(idx+1)
                temp.pop()
                while idx <= len(nums)-2 and nums[idx+1] == nums[idx]:
                    idx += 1
                dfs(idx+1)
        
        dfs(0)
        return res

sol = Solution()
print(sol.subsetsWithDup([1,2,2]))


