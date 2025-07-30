from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def doRecur(intervals):
            res = []
            intervals.sort(key=lambda e:(e[1], e[0]))
            lastInterval = intervals[0]
            pivot = intervals[0][1]
            for s in intervals[1:]:
                if s[0] <= pivot:
                    lastInterval[0] = min(lastInterval[0], s[0])
                    lastInterval[1] = s[1]
                else:
                    res.append(lastInterval)
                    lastInterval = s
                pivot = lastInterval[1]
            res.append(lastInterval)
            return res
        
        res = doRecur(intervals)
        while True:
            nextRes = doRecur(res)
            if res == nextRes:
                break
            else:
                res = nextRes
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for s in intervals[1:]:
            if s[0] <= res[-1][1]:
                res[-1][1] = max(s[1], res[-1][1]) 
            else:
                res.append(s)
        return res




sol = Solution()
print(sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))

