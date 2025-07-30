from math import inf

def findPath():
    n, m = map(int, input().split())
    edges =  []
    for _ in range(m):
        s, e, v = map(int, input().split())
        edges.append([s, e, v])
    
    minDist = [ inf ] * (n+1)
    minDist[1] = 0
    updated = False
    
    for i in range(n):
        for s, e, v in edges:
            if minDist[e] > minDist[s] + v:
                minDist[e] = minDist[s] + v
                if i == n-1:
                    updated = True
    
    if updated:
        return "circle"
    elif minDist[-1] == inf:
        return "unconnected"
    else:
        return minDist[-1]
    

print(findPath())
