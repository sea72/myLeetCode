from typing import List

def mergeSort(nums, low, high):
    if low >= high:
        return 0
    mid = ((high - low) >> 1) + low
    return mergeSort(nums, low, mid) + mergeSort(nums, mid+1, high) + merge(nums, low, mid, high)

def merge(nums: List[int], low, mid, high):
    i, j, k = low, mid + 1, 0
    res = 0
    temp = [None] * (high - low + 1)
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            res += (high - j + 1) * nums[i]
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1
        k += 1
    while i<= mid:
        temp[k] = nums[i]
        k += 1
        i += 1
    while j<= high:
        temp[k] = nums[j]
        k += 1
        j += 1
    for no in range(k):
        nums[no + low] = temp[no]
    return res

nums = [1, 3, 4, 2, 5]
res = mergeSort(nums, 0, len(nums)- 1)
print(nums)
print(res)
        


    

