from typing import List
import bisect

class Solution0:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0
        sums = []
        temp = 0
        ans = len(nums)
        for i in nums:
            temp += i
            sums.append(temp)
        if sums[-1] < target:
            return 0
        while cur < len(nums):
            bound = bisect.bisect_left(sums, target + sums[cur] - nums[cur])
            if bound < len(nums):
                ans = min(ans, bound - cur + 1)
            cur += 1
        return ans

class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        begin, end, curSum = 0, 0, 0
        ans = len(nums) + 1
        while end < len(nums):
            curSum += nums[end]
            while curSum >= target:
                ans = min(ans, end - begin + 1)
                curSum -= nums[begin]
                begin += 1
            end += 1
        return ans if ans < len(nums) + 1 else 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        begin, end, curSum = 0, 0, 0
        ans = len(nums) + 1
        while end < len(nums):
            curSum += nums[end]
            if curSum >= target:
                while curSum >= target:
                    curSum -= nums[begin]
                    begin += 1
                ans = min(ans, end - (begin -1) + 1)
            end += 1
        return ans if ans < len(nums) + 1 else 0

target = 11
nums = [1,2,3,4,5]
print(Solution().minSubArrayLen(target, nums))