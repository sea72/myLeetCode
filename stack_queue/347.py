import collections
from typing import List
class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        return [_[0] for _ in cnt.most_common(k)]

import heapq
class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        priorityQue = []
        for key,value in hashmap.items():
            if len(priorityQue) < k:
                heapq.heappush( priorityQue, (value, key))
            elif priorityQue[0][0] <= value:
                # heapq.heappop()
                # heapq.heappush((value, key))
                heapq.heapreplace(priorityQue, (value, key))
            else:
                pass
        return [ _[1] for _ in priorityQue]
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(nums, low, high):
            pivot = nums[low]
            while low < high:
                while low < high and nums[high] <= pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] >= pivot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            return low


        def myQsort(nums, low, high):
            if low < high:
                pivotLoc = partition(nums, low, high)
                if pivotLoc < k-1:
                    myQsort(nums, pivotLoc+1, high)
                elif pivotLoc > k-1:
                    myQsort(nums, low, pivotLoc-1)
                else:
                    return

        hashmap = collections.defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        hashmap = [(value, key) for key,value in hashmap.items()]
        myQsort(hashmap, 0, len(hashmap)-1)
        return [ _[1] for _ in hashmap[0:k]]


sol = Solution()
print(sol.topKFrequent(nums = [1,2], k = 2))