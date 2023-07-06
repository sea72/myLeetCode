from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [ [None] * n for _ in range(n) ]
        def fillEdge(start, edgeLen, value):
            if edgeLen <= 0:
                pass
            else:
                x, y = start[0], start[1]
                signals = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]
                edgeLens = [edgeLen, edgeLen-1, edgeLen-1, edgeLen-2]
                for i in range(4):
                    for j in range(edgeLens[i]):
                        # if signals[i][0] == 1:
                        #     x += 1
                        # elif signals[i][0] == -1:
                        #     x -= 1
                        # if signals[i][1] == 1:
                        #     y += 1
                        # elif signals[i][1] == -1:
                        #     y -= 1
                        x += signals[i][0]
                        y += signals[i][1]
                        res[x][y] = value
                        value += 1
                fillEdge((x, y), edgeLen - 2, value)
        
        fillEdge((0,-1), n, 1)
        return res

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 预设四个Boundry, up, down, left, right， 每次填的数都有一个维度是boundry，表明了是从外向内而填
        # 填完一列之后，一定会有一个boundry发生改变
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        index = 1
        res = [ [None] * n for _ in range(n) ]
        while(index <= n * n):
            # 从左到右， 上边界减一层
            for i in range(left, right + 1):
                res[up][i] = index
                index += 1
            up += 1

            # 从上到下，右边界减一列
            for i in range(up, down + 1):
                res[i][right] = index
                index += 1
            right -= 1

            # 从右到左，下边界减一层
            for i in range(right, left - 1, -1):
                res[down][i] = index
                index += 1
            down -= 1

            # 从下到上，左边界减一列
            for i in range(down, up - 1 , -1):
                res[i][left] = index
                index += 1
            left += 1
        return res




n = 9
sd = Solution().generateMatrix(n)




