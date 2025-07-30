from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > d[-1]:
                d.append(nums[i])
            else:
                l, r = 0, len(d) - 2
                while l <= r:
                    # mid = l + (r - l) // 2
                    mid = (l + r) >> 1
                    if d[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid - 1
                d[l] = nums[i]
        return len(d)


sol = Solution()
print(sol.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
