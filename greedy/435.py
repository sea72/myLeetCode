from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: 
            return 0
        
        intervals.sort(key=lambda e:e[1])
        pivot = intervals[0][1]
        cnt = 1
        for interval in intervals:
            if interval[0] >= pivot:
                cnt += 1
                pivot = interval[1]
        return len(intervals) - cnt


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: 
            return 0

        intervals.sort(key=lambda e:e[0])
        n = len(intervals)
        f = [1] * n

        for i in range(1, n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    f[i] = max(f[i], f[j] + 1)
        return n - max(f)
    
sol = Solution()
print(sol.eraseOverlapIntervals(intervals=[[1,2],[2,3],[3,4],[1,3]]))
