# from typing import List
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         valueDic = {}
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 value = nums[i]+nums[j]
#                 if value in valueDic:
#                     valueDic[value].append((i,j))
#                 else:
#                     valueDic[value] = []
#                     valueDic[value].append((i,j))
#         for i in nums:
#             if -i in valueDic:
#                 for j,k in valueDic[-i]:
#                     print(i, nums[j], nums[k])

# 主要想法是把每两个元素的和存起来，第三个元素值在字典中直接去找对应的前两个值
# 但是遇到了问题：
# 去重会是一个噩梦级别的操作
# eg. 用set来去重，前两个元素当作set来存储 {2，2} => {2}

# 还是通过笨办法的三层枚举，但是去削减他的次数
from typing import List
class Solution0:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i!= 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums)-1
            for j in range( i+1, len(nums)):
                if j!= i+1 and nums[j] == nums[j-1]:
                    continue
                while k>j and nums[j] + nums[k] > -nums[i]:
                    k -= 1
                if k == j:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
        return res

import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        # nums 借counter()完成了去重，同时保留其重复个数的信息
        nums = sorted(counts)
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                        continue
                else:
                    if -num * 2 in counts:
                        ans.append([num, num, -2 * num])
            if num < 0:
                two_sum = -num
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                for j in nums[left: bisect.bisect_right(nums, (two_sum // 2), left)]:
                    k = two_sum - j
                    if k in counts and k != j:
                        ans.append([num, j, k])

        return ans
    
sd = Solution()
a = sd.threeSum([0, 0, 0, 1, 3, -2, 3, -4, 1])
print(a)
