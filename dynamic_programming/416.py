from typing import List

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         end = len(nums)
#         def doPart(cur, left, right):
#             if cur >= end:
#                 return left == right
#             else:
#                 dvdToLeft = doPart(cur+1, left + nums[cur], right)
#                 dvdToRight = doPart(cur+1, left, right + nums[cur])
#                 return dvdToLeft or dvdToRight

#         return doPart(0, 0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        if target & 1:
            return False
        else:
            target = target // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(len(nums)):
            for j in range(1, target + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)-1][target]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        maxNum = max(nums)

        if target & 1 or maxNum > (target // 2):
            return False
        target = target // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            # 因为此时dp[j] = dp[j]这一式子的特殊性
            # 所以我们提出 dp可以不变的
            # 那么只考虑dp可能发生改变的一个范围去做循环
            # for j in range(target, 0 , -1):
            #     if nums[i] <= j:
            #         dp[j] = dp[j] or dp[j-nums[i]]
            #     else:
            #         dp[j] = dp[j]
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[target]

        




sol = Solution()
print(sol.canPartition(nums = [2,2,1,1]))