from typing import List
from collections import Counter
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         class Node:
#             def __init__(self, val, next = None) -> None:
#                 self.val = val
#                 self.next = next
#         cnt = Counter(nums[:k])
#         temp = sorted(nums[:k])
#         next = None
#         for no in range(len(temp)):
#             head = Node(temp[no], next)
#             next = head
#         slow = 0
#         curr = k
#         res = []
#         while k < len(nums):
#             cnt[nums[slow]] -= 1
#             cnt[nums[curr]] += 1
#             if nums[curr] >= head.val:
#                 newNode = Node(nums[curr], head)
#                 head = newNode
#                 res.append(newNode.val)
#             else:
#                 node = head
#                 while node.val > nums[curr]:
#                     node = node.next

import heapq       
class Solution0:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class MyHeap:
            def __init__(self, nums) -> None:
                self.nums = nums
                self.heapify()

            def adjustDown(self, index):
                while index * 2 + 1 < len(self.nums):
                    if index * 2 + 2 < len(self.nums) and self.nums[index*2+2] > self.nums[index*2+1]:
                        maxChildIndex = index * 2 + 2
                    else:
                        maxChildIndex = index * 2 + 1
                    if self.nums[index] < self.nums[maxChildIndex]:
                        self.nums[index], self.nums[maxChildIndex] = self.nums[maxChildIndex], self.nums[index]
                        index = maxChildIndex
                    else:
                        break

            def heapify(self):
                for index in range(len(self.nums)//2-1, -1, -1):
                    self.adjustDown(index)
            
            def heapInsert(self, newNum):
                self.nums.append(newNum)
                index = len(self.nums) - 1
                while index > 0 and self.nums[index] > self.nums[(index-1)//2]:
                    self.nums[index], self.nums[(index-1)//2] = self.nums[(index-1)//2], self.nums[index]
                    index = (index-1)//2

            def heapPop(self):
                self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
                self.nums.pop()
                # self.heapify()
                self.adjustDown(0)

            def heapTop(self):
                return self.nums[0]

        myheap = MyHeap( [(nums[i], i) for i in range(k)] )
        res = [ myheap.heapTop()[0]]
        for i in range(k, len(nums)):
            myheap.heapInsert((nums[i], i))
            while myheap.heapTop()[1] <= i - k:
                myheap.heapPop()
            res.append(myheap.heapTop()[0])
        return res
    

import collections
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowQue = collections.deque()
        for i in range(k):
            while windowQue and nums[windowQue[-1]] < nums[i]:
                windowQue.pop()
            windowQue.append(i)
        ans = [ nums[windowQue[0]] ]
        for i in range(k, len(nums)):
            while windowQue and nums[windowQue[-1]] < nums[i]:
                windowQue.pop()
            windowQue.append(i)
            while windowQue[0] <= i - k:
                windowQue.popleft()
            ans.append(nums[windowQue[0]])
        return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i-1], nums[i])
        for i in range(n-1, -1, -1):
            if i % k == 0 or i == n-1:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i+1], nums[i])
        # low, high = 0, k-1
        # ans = []
        # while high < n:
        #     temp = max(suffixMax[low], prefixMax[high])
        #     ans.append(temp)
        #     low += 1
        #     high += 1
        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans


sol = Solution()
print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 6))





            

                


                




