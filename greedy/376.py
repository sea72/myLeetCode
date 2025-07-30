from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2 if nums[-1] != nums[-2] else 1
        
        temp  = []
        maxL = 0

        def dfs(startIdx):
            if startIdx == len(nums):
                nonlocal maxL
                maxL = max(len(temp), maxL)
                return 
            for no in range(startIdx, len(nums)):
                if len(temp) >= 2 and (temp[-1] - temp[-2]) * (nums[no] - temp[-1]) > 0:
                    return
                if temp and temp[-1] == nums[no]:
                    return  
                temp.append(nums[no])
                dfs(no+1)
                temp.pop()
        dfs(0)
        return maxL
    
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff
        
        return ret

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = max(up, down + 1)
            elif nums[i] < nums[i - 1]:
                down = max(up + 1, down)
        
        return max(up, down)


sol = Solution()
print(sol.wiggleMaxLength([1,7,4,9,2,5]))


