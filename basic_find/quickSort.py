import random

# def partition(nums, low, high):
#     # temp = (low + high) >> 1
#     temp = random.randint(low, high)
#     pivotValue = nums[temp]
#     pivot = low
#     nums[low], nums[temp] = nums[temp], nums[low]
#     while low < high:
#         while low < high and nums[high] >= pivotValue:
#             high -= 1
#         while low < high and nums[low] <= pivotValue:
#             low += 1
#         if low < high:
#             nums[low], nums[high] = nums[high], nums[low]
#     nums[low], nums[pivot] = nums[pivot], nums[low]
#     return low

def partition(arr, start, end):
    index = random.randint(start, end)
    pivot = arr[index]
    arr[start],arr[index] = arr[index],arr[start]
    i, j = start, end
    while i<j:
        while i<j and arr[j]>=pivot:
            j -= 1
        while i<j and arr[i]<=pivot:
            i += 1
        if i != j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[start], arr[i] = arr[i], arr[start]
    return i

# def partition(nums, low, high):
#     temp = random.randint(low, high)
#     nums[temp], nums[high] = nums[high], nums[temp]
#     pivotValue = nums[high]
#     lessBound = low
#     moveSameValueFlag = 0
#     while low < high:       # make sure the lessBound must be the pivotValue itself
#         if nums[low] < pivotValue or (nums[low] == pivotValue and moveSameValueFlag & 1):
#             moveSameValueFlag += 1
#             nums[lessBound], nums[low] = nums[low], nums[lessBound]
#             lessBound += 1
#         low += 1
#     nums[lessBound], nums[high] = nums[high], nums[lessBound]
#     return lessBound


    
def recurveQuickSort(nums, low, high):
    if low >= high:
        return
    pivot = partition(nums, low, high)
    recurveQuickSort(nums, low, pivot-1)
    recurveQuickSort(nums, pivot+1, high)
   

# def partition(nums, low, high):
#     cur, less, more = low, low-1, high
#     while cur < more:
#         if nums[cur] < nums[high]:
#             less += 1
#             nums[cur], nums[less] = nums[less], nums[cur]
#             cur += 1
#         elif nums[cur] == nums[high]:
#             cur += 1
#         else:
#             more -= 1
#             nums[more], nums[cur] = nums[cur], nums[more]
#     nums[more], nums[high] = nums[high], nums[more]
#     return less + 1, more

# def recurveQuickSort(nums, low, high):
#     if low >= high:
#         return
#     rand = random.randint(low, high)
#     nums[rand], nums[high]  = nums[high], nums[rand]
#     pivots = partition(nums, low, high)
#     recurveQuickSort(nums, low, pivots[0]-1)
#     recurveQuickSort(nums, pivots[1]+1, high)

def quickSort(nums):
    recurveQuickSort(nums, 0, len(nums)-1)
    return nums

success = 0
testCount = 10000
for _ in range(testCount):
    
    temp = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
    nums = temp[:]
    nums = quickSort(nums)
    temp.sort()

    if temp != nums:
        print(nums)
    else:
        success += 1
print(success == testCount)
# nums = [1, 2, 2, 2, 3, 1, 4]
# print(quickSort(nums))