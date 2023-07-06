from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i!= 0 and nums[i] == nums[i-1]:
                continue
            # 剪枝
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3] < target:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                # 剪枝
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[len(nums)-1] + nums[len(nums)-2] < target:
                    continue
                remain = target - nums[i] - nums[j]
                k = j+1
                l = len(nums) - 1
                while k < l:
                    if nums[k] + nums[l] == remain:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                        l -= 1
                    elif nums[k] + nums[l] < remain:
                        k += 1
                    elif nums[k] + nums[l] > remain:
                        l -= 1
                    # else:
                    #     while k < l and nums[k] + nums[l] < remain:
                    #         k += 1
                    #     while k < l and nums[k] + nums[l] > remain:
                    #         l -= 1
        return res
    
sd = Solution()
a = sd.fourSum([1,0,-1,0,-2,2], 0)
print(a)
                

