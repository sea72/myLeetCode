from typing import List
# class Solution:
#     def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
#         hourLeft = hour - len(dist) + 1
#         def hourUseBeforeLast(v, nums = dist[0:-1]):
#             hourUse = 0
#             for item in nums:
#                 temp = item // v
#                 tempHour = temp if temp * v == item else temp + 1
#                 hourUse += tempHour
#             return hourUse
        
#         if hourLeft < 0:
#             return -1
#         else:
#             vMax = 10**7
#             vMin = 1
#             while vMin < vMax:
#                 vMid = (vMin + vMax) // 2
#                 if hourUseBeforeLast(vMid) + dist[-1] / vMid <= hour:
#                     vMax = vMid
#                 else:
#                     vMin = vMid + 1
#             return vMin

from bisect import bisect_left 
import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            res = 0
            for i, d in enumerate(dist):
                res += (d / speed) if i == len(dist) - 1 else math.ceil(d / speed)
            return res <= hour

        r = 10**7 + 1
        ans = bisect_left(range(1, r), True, key = check) + 1 # bisect always return the index rather than value
        return -1 if ans == r else ans
    
sd = Solution()
dist = [5,3,4,6,2,2,7]
hour = 10.92
res = sd.minSpeedOnTime(dist, hour)
print(res)