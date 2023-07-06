import bisect
nums = [-5, -4, -1, 3, 4, 4, 4, 5, 6, 7, 9]
target= 4
# left, right = 0, len(nums)
# while left < right:
#     mid = (left + right) >> 1 
#     if nums[mid] >= target:
#         right = mid
#     else:
#         left = mid + 1
# print(left, nums[left])
low = bisect.bisect_left(nums, 4)
high = bisect.bisect(nums, 4)
print(low, nums[low])
print(high, nums[high])



