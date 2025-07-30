from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrowTarget = []
        points.sort(key=lambda e:e[0])
        for new in points:
            needInsert = True
            for no in range(len(arrowTarget)):
                if arrowTarget[no][1] >= new[1]:
                    arrowTarget[no] = new
                    needInsert = False
                    break
                if arrowTarget[no][1] >= new[0]:
                    arrowTarget[no] = [new[0], arrowTarget[no][1]]
                    needInsert = False
                    break
            if needInsert:
                arrowTarget.append(new)
        return len(arrowTarget)
    

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda e:e[1])
        ptr = points[0][1]
        cnt = 1
        for point in points:
            if point[0] > ptr:
                cnt += 1
                ptr = point[1]
        return cnt


sol = Solution()
points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(sol.findMinArrowShots(points=points))

                

    