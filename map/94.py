from math import inf

# def findPath():
#     n, m = map(int, input().split())
#     edges = []
#     for _ in range(m):
#         s, e, v = map(int, input().split())
#         edges.append([s, e, v])

#     minDist = [ inf ] * (n+1)
#     minDist[1] = 0
    
#     for _ in range(n-1):
#         updated = False
#         for s, e, v in edges:
#             if minDist[s] < inf and minDist[s] + v < minDist[e]:
#                 minDist[e] = minDist[s] + v
#                 updated = True
#         if not updated:
#             break
    
#     if minDist[n] < inf:
#         print(minDist[n])
#     else:
#         print('unconnected')

# findPath()

from collections import deque
def findPath2():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, v = map(int, input().split())
        edges[s].append([e, v])
    que = deque([1])
    visited = [False] * (n+1)
    minDist = [ inf ] * (n+1)
    minDist[1] = 0
    visited[1] = True

    while que:
        cur = que.popleft()
        visited[cur] = False
        for e,v in edges[cur]:
            minDist[e] = min(minDist[cur]+v, minDist[e])
            if not visited[e]:
                que.append(e)
                visited[e] = True

    if minDist[n] < inf:
        print(minDist[n])
    else:
        print('unconnected')

findPath2()
