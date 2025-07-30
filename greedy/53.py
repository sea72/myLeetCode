from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        一种贪心思想
        只继承资产，不继承债务
        如果有负资产（债务）, 那就直接清零
        如果有正资产,那可以保留后继续累加资产,又因为新累加的可能是负数,所以要用一个res来保存曾经出现的某个最大值
        '''
        temp = 0
        res = -math.inf
        for no in nums:
            if temp < 0:
                temp = no
            else:
                temp += no
            res = max(res, temp)
        return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        maxAns = nums[0]
        for x in nums: 
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns
    


sol = Solution()
print(sol.maxSubArray([3,4,5,-20,1,2]))