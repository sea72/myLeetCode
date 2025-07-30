from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []
        used = [0] * len(nums)

        def dfs():
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            levelUsed = set()
            for no in range(len(nums)):
                if used[no] == 0:
                    if nums[no] not in levelUsed:
                        used[no] = 1
                        temp.append(nums[no])
                        levelUsed.add(nums[no])
                        dfs()
                        temp.pop()
                        used[no] = 0
        dfs()
        return res
    

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []
        used = [0] * len(nums)

        def dfs():
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for no in range(len(nums)):
                if used[no] or (no > 0 and nums[no] == nums[no-1] and not used[no-1]):
                    continue
                temp.append(nums[no])
                used[no] = 1
                
                dfs()

                used[no] = 0
                temp.pop()

        nums.sort()         
        dfs()
        return res

sol = Solution()
print(sol.permuteUnique([3,3,0,3]))
                