from typing import List
import math 
from collections import Counter
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        minAbs = math.inf
        negNums = []
        res =  0
        for i in nums:
            if i >= 0 :
                if i < minAbs:
                    minAbs = i
            else:
                negNums.append(i)
            res += i
        negNums.sort(reverse=True)
        while k > 0 and negNums:
            k -= 1
            choose = negNums.pop() * (-1)
            res += choose * 2
            if choose < minAbs:
                minAbs = choose
        return res - 2 * minAbs if k & 1 == 1 else res


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break
        
        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break
        
        return ans


sol = Solution()
nums = [-2,9,9,8,4]
k = 5
print(sol.largestSumAfterKNegations(nums, k))


                

        

