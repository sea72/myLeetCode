import functools
import random
import time

def testSort(func):
    @functools.wraps(func)
    def tester():
        success = 0
        startTime = time.perf_counter()
        for i in range(5):
            tempList = [random.randint(0, 100000) for _ in range(10000)]
            officialSort = sorted(tempList)
            if func(tempList) == officialSort:
                success += 1
        endTime =  time.perf_counter()
        elapsed = endTime - startTime
        if success == 5:
            print(f'Success in {func.__name__} with {elapsed:.6f} seconds')
        else:
            print(f'Wrong in {func.__name__}')
            print(f'Your sort is {tempList}')
            print(f'Official sort is {officialSort}')
    return tester

@testSort
def straightInsertSort(nums):
    # 向前查找有两个退出情况
    # 实际上每次都是在找填入j+1的那个数
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            temp = nums[i]
            # for j in range(i-1, -1, -1)  wrong, j need to be -1
            # for j in range(i-1, -2, -1)  wrong, j = -1 shouldn't enter the loop
            j = i - 1
            while j >= 0:
                if temp < nums[j]:
                    nums[j+1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j+1] = temp
    return nums

@testSort
def binaryInsertSort(nums):
    # 1.low<=high 表征一个左右包含区间
	# 2.必须令high = mid-1  low = mid+1，否则循环会进入死循环，即手动来创造一个退出条件
    # 3.间接也实现了和mid值的对比，最终的插入位置在low位或者high+1位
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            temp = nums[i]
            low, high = 0, i-1
            while low <= high:
                mid = (low + high) >> 1
                if temp < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            for j in range(i-1, high, -1):
                nums[j+1] = nums[j]
            nums[low] = temp
    return nums
            


@testSort
def bubbleSort(nums):
    for end in range(len(nums)-1, 0, -1):
        hasMoved = False
        for i in range(0, end):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
                hasMoved = True
        if not hasMoved:
            break
    return nums

@testSort
def simpleSelectionSort(nums):
    for target in range(len(nums)):
        minLoc = target
        min = nums[target]
        i = target + 1
        while i < len(nums):
            if nums[i] < min:
                minLoc = i
                min = nums[i]
            i += 1
        nums[target], nums[minLoc] = nums[minLoc], nums[target]
    return nums

@testSort
def shellSort(nums):
    delta = len(nums) // 2
    while delta >= 1:
        for i in range(delta, len(nums), 1):
            if nums[i] < nums[i-delta]:
                temp = nums[i]
                j = i - delta
                while j >= 0 and temp < nums[j]:
                    nums[j+delta] = nums[j]
                    j = j - delta
                nums[j+delta] = temp
        delta = delta // 2
    return nums

def partition(nums, low, high):
    temp = low
    pivot = nums[low]
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        while low < high and nums[low] <= pivot:
            low += 1
        if low < high:
            nums[high], nums[low] = nums[low], nums[high]
    # end when low == high
    # and ignore nums[low]'s correct position
    # just send pivot to right position
    # which means 1 round make right position for 1 num
    nums[low], nums[temp] = nums[temp], nums[low]


    
    return low


def recurveQuickSort(nums, low, high):
    if low < high:
        pivotLoc = partition(nums, low, high)
        recurveQuickSort(nums, low, pivotLoc-1)
        recurveQuickSort(nums, pivotLoc+1, high)

def iterativeQuickSort(nums):
    low, high = 0, len(nums)-1
    ranges = [(low, high)]
    while ranges:
        low, high = ranges[-1][0], ranges[-1][1]
        ranges.pop()
        if low < high:
            pivotLoc = partition(nums, low, high)
            if pivotLoc > low + 1:
                ranges.append((low, pivotLoc - 1))
            if pivotLoc + 1 < high:
                ranges.append((pivotLoc+1 , high))

 
@testSort
def quickSort(nums):
    # recurveQuickSort(nums, 0, len(nums)-1)
    # return nums
    iterativeQuickSort(nums)
    return nums

def doMerge(nums, low, mid, high):
    tempList = [None] * (high - low + 1)
    i, j, k = low, mid+1, 0
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            tempList[k] = nums[i]
            i += 1
        else:
            tempList[k] = nums[j]
            j += 1
        k += 1
    while j<= high:
        tempList[k] = nums[j]
        k += 1
        j += 1
    while i <= mid:
        tempList[k] = nums[i]
        k += 1
        i += 1
    nums[low:high+1] = tempList
    

def recurveMerge(nums, low, high):
    if low < high:
        mid = (low + high) >> 1
        recurveMerge(nums, low, mid)
        recurveMerge(nums, mid+1, high)
        doMerge(nums, low, mid, high)


@testSort
def mergeSort(nums):
    recurveMerge(nums, 0, len(nums) -1)
    return nums


def adjustDown(nums, item, end):
    while item * 2 + 1 <= end:
        if item*2 + 2 <= end and nums[item*2+2] > nums[item*2+1]:
            maxOfChild = item*2+2
        else:
            maxOfChild = item*2+1
        if nums[item] < nums[maxOfChild]:
            nums[item], nums[maxOfChild] = nums[maxOfChild], nums[item]
            item = maxOfChild
        else:
            break

@testSort
def heapSort(nums):
    for i in range(len(nums)//2 - 1, -1, -1):
        adjustDown(nums, i, len(nums)-1)
    i = len(nums) - 1
    while i >= 0:
        nums[0], nums[i] = nums[i], nums[0]
        i -= 1
        adjustDown(nums, 0, i)
    return nums

def maxBits(nums):
    maxItem = max(nums)
    digits = 0
    while maxItem != 0:
        maxItem //= 10
        digits += 1
    return digits

def getBit(num, i):
    res = 0
    while i >= 0:
        res = num % 10
        num //= 10
        i -= 1
    return res

def doRadixSort(nums, digit):
    tempList = [None] * len(nums)
    for i in range(digit):
        counter = [0] * 10
        for item in nums:
            bit = getBit(item, i)
            counter[bit] += 1

        for cntNo in range(len(counter)):
            counter[cntNo] += counter[cntNo - 1] if cntNo > 0 else 0

        for item in nums[::-1]:
            bit = getBit(item, i)
            tempList[counter[bit] - 1] = item
            counter[bit] -= 1
        # it will cover the origin nums, however can't modify function's father's nums
        # nums = tempList
        for no in range(len(tempList)):
            nums[no] = tempList[no]

@testSort
def radixSort(nums):
    if len(nums) < 2:
        return nums
    doRadixSort(nums, maxBits(nums))
    return nums

@testSort
def officialSort(nums):
    return sorted(nums)

if __name__ == "__main__":
    straightInsertSort()
    binaryInsertSort()
    bubbleSort()
    simpleSelectionSort()
    shellSort()
    quickSort()
    mergeSort()
    heapSort()
    radixSort()
    officialSort()