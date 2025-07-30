from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for no in range(2, len(nums)):
            first, second = second, max(first + nums[no], second)
        return second
    
sol = Solution()
print(sol.rob([2,1,1,3]))
