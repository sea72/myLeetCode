from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lhs, rhs = 0, len(nums)
        while(lhs < rhs):
            if nums[lhs] == val:
                nums[lhs] = nums[rhs-1]
                rhs -= 1
            else:
                lhs += 1
        return lhs


sd = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sd.removeElement(nums, val))









            




                