from typing import List


class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.tree = [0] * (4 * n)
        self.build(data, 1, 0, n-1)
    
    def build(self, data, cur, start, end):
        if start == end:
            self.tree[cur] = data[start]
            return 
        mid = (start + end) // 2
        self.build(data, cur * 2, start, mid)
        self.build(data, cur * 2 + 1, mid+1, end)


    def pushUp(self, cur):
        self.tree[cur] = max(self.tree[cur*2], self.tree[cur*2+1])

    def findFirstAndUpdate(self, cur, start, end, value):
        if self.tree[cur] < value:
            return -1
        if start == end:
            self.tree[cur] = -1
            return start
        mid = (start + end) // 2
        i = self.findFirstAndUpdate(cur*2, start, mid, value)
        if i == -1:
            i = self.findFirstAndUpdate(cur*2+1, mid+1, end, value)
        self.pushUp(cur)
        return i

                


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        
        


                        
        

        

        

