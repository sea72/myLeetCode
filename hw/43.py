h, w = list(map(int, input().split()))
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))
visited = [ [False] * w for _ in range(h)]

directions = [[-1, 0 ], [1, 0] ,[ 0, -1], [ 0, 1]]

def distance(point):
    return ((h-1-point[0]) **2 + (w-1-point[1]) ** 2) ** 0.5

path = [(0,0)]

def dfs(cur, path, visited):
    visited[cur[0]][cur[1]] = True
    if cur == (h-1, w-1):
        return path
    nextPoints = []
    for addX, addY in directions:
        nextX, nextY = cur[0] + addX, cur[1] + addY
        if 0 <= nextX <= h -1 and 0<= nextY <= w-1 and not visited[nextX][nextY] and graph[nextX][nextY] == 0:
            nextPoints.append((cur[0] + addX, cur[1] + addY))
    nextPoints.sort(key = lambda e: distance(e))
    for np in nextPoints:
        path.append(np)
        temp = dfs(np, path, visited)
        if temp:
            return temp
        else:
            path.pop(-1)
            visited[np[0]][np[1]] = False
    return None

res = dfs((0,0), path, visited)
for p in res:
    print(p)
            

