from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        theSum = sum(nums)

        # 1.target可能完全无意义，不落在可能的范围值内
        if abs(target) > theSum:
            return 0
        
        # 2.sum可能为负数，但负数是无法做数组下标的
        # 这里考虑加一个偏移量来解决这个问题
        dp = [ [0] * (2 * theSum + 1) for _ in range(len(nums))]

        # 3.一个数自身正负从而产生两个结果
        # 不能忽视 +0 与 -0 是两个结果
        dp[0][nums[0] + theSum] += 1
        dp[0][-nums[0] + theSum] += 1

        for i in range(1, len(nums)):
            for j in range(2 * theSum + 1):
                # 4. 考虑针对某个和J，其只存在单边来源的可能性，另一边是完全超限的，无意义的
                byPlus = dp[i-1][j - nums[i]] if j - nums[i] >= 0 else 0
                byMinus = dp[i-1][j + nums[i]] if j + nums[i] <= 2 * theSum else 0
                dp[i][j] = byPlus + byMinus

        # 5. 返回结果也不要忘了偏移值
        return dp[len(nums)-1][target + theSum]



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        absSum = sum(nums)
        # not so elegant

        # negSum = (absSum - target) / 2
        # # if negSum % 1 != 0 or negSum < 0:
        # #     return 0
        # # negSum = int(negSum)

        negSum = absSum - target
        if negSum % 2 != 0 or negSum < 0:
            return 0
        negSum = negSum // 2
        dp = [0] * (negSum + 1)
        dp[0] = 1
        # the way of increment from 1 is not possible
        # cause you can't control the first element's value
        # when you need 0, you will only initialize one element
        # in such case, you use dp[n[i]] to initialize the dp array, the index overflow will happen
        # so you can choose increment from 0, that's to say, the senario of there's not any element, of course, its value is 1
        for i in range(0, len(nums)):
            # we need dp[i-1][j-nums[i]], but only dp[i][j-nums[i]] left
            # so we should leave dp[i-1][j-nums[i]] untouched so that it can keep the old value
            # for j in range(nums[i], negSum + 1):
            #     dp[j] = dp[j] + dp[j-nums[i]]

            for j in range(negSum, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]

        return dp[negSum]

sol = Solution()
print(sol.findTargetSumWays(nums = [0,0,0,0,0,0,0,0,1], target = 1))
