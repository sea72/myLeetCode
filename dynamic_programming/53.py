from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for no in range(1, len(nums)):
            if dp[no-1] < 0:
                dp[no] = nums[no]
            else:
                dp[no] = dp[no-1] + nums[no]
        
        return max(dp)

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


