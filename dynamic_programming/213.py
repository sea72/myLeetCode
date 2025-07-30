from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robInRange(start, end):
            first, second = nums[start], max(nums[start], nums[start+1])
            for no in range(start+2, end+1):
                first, second = second, max(second, first + nums[no])
            return second
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return robInRange(0, 1)
        else:
            return max(robInRange(0, len(nums)-2), robInRange(1, len(nums)-1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second
        
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, length - 2), robRange(1, length - 1))


sol = Solution()
print(sol.rob([2,3,2]))