from collections import deque
from math import inf

def calculateIslands():
    n, m = map(int, input().split())
    grids = []
    for _ in range(n):
        grids.append( list(map(int, input().split())) )
    visited = [ [False] * m for _ in range(n)]
    directions = [ [1, 0], [0, 1], [-1, 0], [0, -1]]

    res = 0

    def bfs(i, j):
        
        que = deque([])
        visited[i][j] = True
        que.append([i, j])
        nonlocal area

        while(que):
            x, y = que.popleft()
            for addX, addY in directions:
                nextX, nextY = x + addX, y + addY
                if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                    continue
                if not visited[nextX][nextY] and grids[nextX][nextY] == 1:
                    visited[nextX][nextY] = True
                    que.append([nextX, nextY])
                    
                    if nextX == 0 or nextX == n-1 or nextY == 0 or nextY == m-1:
                        area = -inf
                    else:
                        area += 1
                    


    area = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and grids[i][j] == 1:
                area = 1
                bfs(i, j)
                if area > 0:
                    res += area

    
    print(res)


if __name__ == "__main__":
    calculateIslands()



position = [[1, 0], [0, 1], [-1, 0], [0, -1]]
count = 0

def dfs(grid, x, y):
    global count
    grid[x][y] = 0
    count += 1
    for i, j in position:
        next_x = x + i
        next_y = y + j
        if next_x < 0 or next_y < 0 or next_x >= len(grid) or next_y >= len(grid[0]):
            continue
        if grid[next_x][next_y] == 1: 
            dfs(grid, next_x, next_y)
                
n, m = map(int, input().split())

# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

# 清除边界上的连通分量
for i in range(n):
    if grid[i][0] == 1: 
        dfs(grid, i, 0)
    if grid[i][m - 1] == 1: 
        dfs(grid, i, m - 1)

for j in range(m):
    if grid[0][j] == 1: 
        dfs(grid, 0, j)
    if grid[n - 1][j] == 1: 
        dfs(grid, n - 1, j)
    
count = 0 # 将count重置为0
# 统计内部所有剩余的连通分量
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            dfs(grid, i, j)
            
print(count)


from collections import deque

# 处理输入
n, m = list(map(int, input().split()))
g = []
for _ in range(n):
    row = list(map(int, input().split()))
    g.append(row)

# 定义四个方向、孤岛面积（遍历完边缘后会被重置）
directions = [[0,1], [1,0], [-1,0], [0,-1]]
count = 0

# 广搜
def bfs(r, c):
    global count
    q = deque()
    q.append((r, c))
    g[r][c] = 0
    count += 1

    while q:
        r, c = q.popleft()
        for di in directions:
            next_r = r + di[0]
            next_c = c + di[1]
            if next_c < 0 or next_c >= m or next_r < 0 or next_r >= n:
                continue
            if g[next_r][next_c] == 1:
                q.append((next_r, next_c))
                g[next_r][next_c] = 0
                count += 1


for i in range(n):
    if g[i][0] == 1: 
        bfs(i, 0)
    if g[i][m-1] == 1: 
        bfs(i, m-1)

for i in range(m):
    if g[0][i] == 1: 
        bfs(0, i)
    if g[n-1][i] == 1: 
        bfs(n-1, i)

count = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 1: 
            bfs(i, j)

print(count)