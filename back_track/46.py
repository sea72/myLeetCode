from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []

        def dfs(remain):
            if remain == 0:
                res.append(temp[:])
                return 
            for no in range(len(nums)):
                if used[no] == 0:
                    used[no] = 1
                    temp.append(nums[no])
                    dfs(remain-1)
                    temp.pop()
                    used[no] = 0

        used = [0] * len(nums)
        dfs(len(nums))
        return res


sol = Solution()
print(sol.permute([1,2,3]))

        
            
            