from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lhs, rhs = 0, len(nums)-1
        temp = [it**2 for it in nums]
        if nums[lhs] >= 0:
            return temp
        elif nums[rhs] <= 0:
            return temp[::-1]
        else:
            res = [None] * len(temp)
            cur = len(temp)-1
            while lhs <= rhs:
                if temp[lhs] > temp[rhs] :
                    res[cur] = temp[lhs]
                    lhs += 1
                else:
                    res[cur] = temp[rhs]
                    rhs -= 1
                cur -= 1
            return res

nums = [-7,-3,2,3,11]
sd = Solution().sortedSquares(nums)
print(sd)


