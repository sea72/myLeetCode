from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLoc = {}
        for no in range(len(nums)):
            other = target - nums[no]
            if other in numLoc:
                return [no, numLoc[other]] 
            else:
                numLoc[nums[no]] = no
        return []

sol = Solution()
nums = [2,7,11,15]
target = 9
ans = sol.twoSum(nums, target)
print(ans)


