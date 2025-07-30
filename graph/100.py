from collections import deque

# def maxIsland():
#     n, m = map(int, input().split())
#     grids = []
#     directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     for _ in range(n):
#         grids.append( list(map(int, input().split())) )
#     visited = [ [False] * m for _ in range(n)]

#     def bfs(i, j):
#         que = deque([])
#         que.append([i, j])
#         visited[i][j] = True
#         temp = 1
        
#         while(que):
#             x, y = que.popleft()
#             for addX, addY in directions:
#                 nextX, nextY = x + addX, y + addY
#                 if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
#                     if grids[nextX][nextY] == 1 and not visited[nextX][nextY]:
#                         visited[nextX][nextY] = True
#                         que.append([nextX, nextY])
#                         temp += 1
#         return temp

#     res = 0
#     for i in range(n):
#         for j in range(m):
#             if grids[i][j] == 1 and not visited[i][j]:
#                 temp = bfs(i, j)
#                 res = max(res, temp)

#     print(res)



def maxIsland():
    n, m = map(int, input().split())
    grids = []
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for _ in range(n):
        grids.append( list(map(int, input().split())) )
    visited = [ [False] * m for _ in range(n)]

    def bfs(i, j):
        que = deque([])
        que.append([i, j])
        visited[i][j] = True
        nonlocal temp
        
        while(que):
            x, y = que.popleft()
            for addX, addY in directions:
                nextX, nextY = x + addX, y + addY
                if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
                    if grids[nextX][nextY] == 1 and not visited[nextX][nextY]:
                        visited[nextX][nextY] = True
                        que.append([nextX, nextY])
                        temp += 1

    res = 0
    temp = 0
    for i in range(n):
        for j in range(m):
            if grids[i][j] == 1 and not visited[i][j]:
                temp = 1
                bfs(i, j)
                res = max(res, temp)

    print(res)

if __name__ == "__main__":
    maxIsland()