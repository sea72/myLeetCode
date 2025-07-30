from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 0

        # mostR is the rightest of haven't stepped
        mostR = 0
        
        # end is the rightest of have stepped
        end = 0

        for i in range(len(nums)):
            if i > end:
                end = mostR
                step += 1
            mostR = max(mostR, i + nums[i])
            if end >= len(nums)-1:
                break
        return step
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


nums = [2,3,1,1,4]
sol = Solution()
print(sol.jump(nums=nums))
