import heapq
from math import inf


def findShortestPathLen():
    moves = [[-2,-1], [-1,-2], [1,-2], [2,-1], [2,1], [1,2], [-1,2], [-2,1]]
    n = int(input())
    question = []
    for _ in range(n):
        a1, a2, b1, b2 = map(int, input().split())
        question.append([a1, a2, b1, b2])

    def euclideanDis(a1, a2, b1, b2):
        return ((a1-b1)**2 + (a2-b2)**2) ** 0.5


    for a1, a2, b1, b2 in question:
        que = [ [ euclideanDis(a1, a2, b1, b2), a1, a2, ] ]
        step = {(a1, a2):0}
        while que:
            _, curX, curY = heapq.heappop(que)
            if curX == b1 and curY == b2:
                break
            for addX, addY in moves:
                nextX, nextY = curX + addX, curY + addY
                if 1<= nextX <= 1000 and 1 <= nextY <= 1000:
                    stepNew = step[(curX, curY)] + 1
                    if stepNew < step.get((nextX, nextY), inf):
                        step[(nextX, nextY)] = stepNew
                        dis = stepNew + euclideanDis(nextX, nextY, b1, b2)
                        heapq.heappush(que, [dis, nextX, nextY ])
        print(step[(curX, curY)])
                
findShortestPathLen()
