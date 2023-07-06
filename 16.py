        #     while j < k:
        #         while k > j and ds(i,j,k) > 0:
        #             k -= 1
        #         if k == len(nums)-1:
        #             res = smallerAbs(res, ds(i, j, k))
        #         elif k > j:
        #             res = smallerAbs(smallerAbs(ds(i, j, k), ds(i,j,k+1)), res)
        #         if j == k:
        #             res = smallerAbs(res, ds(i, j, k+1))
        #             break

        #         while k > j and ds(i,j,k) < 0:
        #             j += 1
        #         if j == i+1:
        #             res = smallerAbs(res, ds(i, j, k))
        #         elif k > j:
        #             res = smallerAbs(smallerAbs(ds(i, j-1, k), ds(i, j, k)), res)

        #         if j == k:
        #             res = smallerAbs(res, ds(i, j-1, k))
        #             break
        #         if res == 0:
        #             return target
        # return res + target




from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        res = 2**31-1

        def smallerAbs(i, j):
            return i if abs(i) < abs(j) else j

        for i in range(len(nums)):
            if i!= 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums)-1
            j = i + 1

            while j < k:
                temp = nums[i] + nums[j] + nums[k] - target
                res = smallerAbs(res, temp)
                if res == 0:
                    return res + target
                elif temp > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif temp < 0:
                    j += 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
        return res + target

    
sd = Solution()
a = sd.threeSumClosest([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -14)
print(a)