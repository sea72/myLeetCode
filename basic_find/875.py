from typing import List
from math import ceil
from bisect import bisect_left

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # maxK = max(piles)
        # def isRight(k):
        #     temp = 0
        #     # for i in piles:
        #     #     temp += ceil(i/k)
        #     # return temp <= h
        #     return sum(ceil(i/k) for i in piles) <= h
        # left, right = 1, maxK
        # while left < right:
        #     mid = (left + right) >> 1
        #     if isRight(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left
        return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))



sd = Solution()
piles = [30,11,23,4,20]
h = 6
print(sd.minEatingSpeed(piles, h))

