from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            if nums[i] + nums[i + 1] + nums[i+2] + nums[i+3] > target:
                break
            for j in range(i+1, len(nums)-2):
                if j!= i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                remain = target - nums[i] - nums[j]
                high = len(nums) - 1
                low = j + 1
                while high > low:
                    if nums[low] + nums[high] == remain:
                        ans.append([nums[i], nums[j], nums[low], nums[high]])
                        while high > low and nums[low] == nums[low+1]:
                            low += 1
                        low += 1
                        while high > low and nums[high] == nums[high-1]:
                            high -= 1
                        high -= 1
                    else:
                        while high > low and nums[low] + nums[high] > remain:
                            high -= 1
                        while high > low and nums[low] + nums[high] < remain:
                            low += 1
        return ans

sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(sol.fourSum(nums, target))