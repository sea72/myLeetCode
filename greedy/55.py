from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        maxL = 0
        for no in range(len(nums)):
            if maxL < no:
                return False
            maxL = max(maxL, no + nums[no])
            if maxL >= len(nums) - 1:
                return True
        return False
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxL = 0
        for no in range(len(nums)):
            if no <= maxL:
                maxL = max(maxL, no+nums[no])
                if maxL >= len(nums)-1:
                    return True
        return False

    
nums = [2,3,1,1,4]
sol = Solution()
print(sol.canJump(nums=nums))