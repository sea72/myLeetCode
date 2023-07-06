from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

nums = [0,0,1,1,1,2,2,3,3,4]
sd = Solution().removeDuplicates(nums)
print(sd)
print(nums)
