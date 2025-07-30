from math import inf

def findPath():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, v = map(int, input().split())
        edges.append([s, e, v])
    start, end, k = map(int, input().split())

    minDist = [ inf ] * (n+1)
    minDist[start] = 0
    
    for _ in range(k+1):
        minDistCopy = minDist.copy()

        for s, e, v in edges:
            if minDist[e] > minDistCopy[s] + v:
                minDist[e] = minDistCopy[s] + v
    
    return "unreachable" if minDist[end] == inf else minDist[end]


print(findPath())
