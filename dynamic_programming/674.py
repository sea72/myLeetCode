from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur = 0
        maxLen = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]: 
                cur = i
            maxLen = max(maxLen, i - cur + 1)
        return maxLen

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)

sol = Solution()
print(sol.findLengthOfLCIS([1,3,5,4,7]))

