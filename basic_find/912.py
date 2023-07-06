from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, low, mid, high):
            i, j, k = low, mid+1, low
            tempList = [0] * (high + 1)
            while i<= mid and j <= high:
                if nums[i] < nums[j]:
                    tempList[k] = nums[i]
                    i += 1
                else:
                    tempList[k] = nums[j]
                    j += 1
                k += 1
            while i <= mid:
                tempList[k] = nums[i]
                k += 1
                i += 1
            while j <= high:
                tempList[k] = nums[j]
                k += 1
                j += 1
            no = low
            while no <= high:
                nums[no] = tempList[no]
                no += 1

        def mergeSort(nums, low, high):
            if low < high:
                mid = (low + high) // 2
                mergeSort(nums, low, mid)
                mergeSort(nums, mid + 1, high)
                merge(nums, low, mid, high)

        mergeSort(nums, 0, len(nums)-1)
        return nums
    
    def bubbleSortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        i = len(nums)-1
        while i > 0:
            swapFlag = False
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j]  = nums[j], nums[j+1]
                    swapFlag = True
            if swapFlag == False:
                break
            i -= 1
        return nums
    

    
    def quickSort(self, nums : List[int]) -> List[int]:
        def partition(nums, low, high):
            pivotValue = nums[low]
            while low < high:
                while low < high and nums[high] >= pivotValue:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] <= pivotValue :
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivotValue
            return low
        
        def recurveQuickSort(nums, low, high):
            if low < high:
                pivot = partition(nums, low ,high)
                recurveQuickSort(nums, low, pivot - 1)
                recurveQuickSort(nums, pivot + 1, high)
            
        recurveQuickSort(nums, 0, len(nums)-1)
        return nums


if __name__ == "__main__":
    # import json
    # with open(r"d:/Lab/codes/leetcode/basic_find/data.txt", 'r') as f:
    #     nums = json.loads(f.read())
    #     print(len(nums))
    import random
    nums = [ random.randint(-50000, 50000) for _ in range(50000)]
    nums.sort()
    sd = Solution()
    import time
    start = time.time()
    res = sd.quickSort(nums)
    end = time.time()
    print(end-start)
    # print(nums)
    # print(res == temp)
