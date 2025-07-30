from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dfs(idx):
            used = [False] * 201
            if len(temp) >= 2:
                res.append(temp[:])
            for no in range(idx, len(nums)):
                if (temp and nums[no] < temp[-1]) or used[nums[no] + 100] == True:
                    continue
                temp.append(nums[no])
                used[nums[no] + 100 ] = True
                dfs(no+1)
                temp.pop()

        dfs(0)
        return res
    
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dfs(cur):

            # specify if it is the right choice
            if cur == len(nums):
                if len(temp) >= 2:
                    res.append(temp[:])
                return
            
            # specify if to choose it
            if not temp or nums[cur] >= temp[-1]:
                temp.append(nums[cur])
                dfs(cur+1)
                temp.pop()

            # specify if to ingore it 
            if not temp or nums[cur] != temp[-1]:
                dfs(cur+1)
        dfs(0)
        return res

sol = Solution()
print(sol.findSubsequences([1,7,7]))