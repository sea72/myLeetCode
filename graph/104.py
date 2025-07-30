from collections import defaultdict

def makeLargestIsland():
    n, m = map(int, input().split())
    grids = []
    for _ in range(n):
        grids.append(list(map(int, input().split())))
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    mark = 1
    area = 0
    islandHashMap = defaultdict(lambda:0)
    maxIsland = 0
    maxArea = 0

    def dfs(i, j, mark):
        nonlocal area
        grids[i][j] = mark
        area += 1
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m-1:
                continue
            if grids[nx][ny] == 1:
                dfs(nx, ny, mark)


    for i in range(n):
        for j in range(m):
            if grids[i][j] == 1:
                mark += 1
                area = 0
                dfs(i, j, mark)
                islandHashMap[mark] = area
                maxArea = max(maxArea, area)

    
    for i in range(n):
        for j in range(m):
            if grids[i][j] == 0:
                neighbor = set()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if x < 0 or x > n-1 or y < 0 or y > m -1:
                        continue
                    neighbor.add(grids[x][y])
                maxIsland = max(maxIsland, sum(map(lambda e: islandHashMap[e], neighbor)))

    print(max(maxIsland + 1, maxArea))


if __name__ == "__main__":
    makeLargestIsland()


import collections

directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
area = 0

def dfs(i, j, grid, visited, num):
    global area
    
    if visited[i][j]:
        return

    visited[i][j] = True
    grid[i][j] = num  # 标记岛屿号码
    area += 1
    
    for x, y in directions:
        new_x = i + x
        new_y = j + y
        if (
            0 <= new_x < len(grid)
            and 0 <= new_y < len(grid[0])
            and grid[new_x][new_y] == "1"
        ):
            dfs(new_x, new_y, grid, visited, num)
    

def main():
    global area
    
    N, M = map(int, input().strip().split())
    grid = []
    for i in range(N):
        grid.append(input().strip().split())
    visited = [[False] * M for _ in range(N)]
    rec = collections.defaultdict(int)
    
    cnt = 2
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "1":
                area = 0
                dfs(i, j, grid, visited, cnt)
                rec[cnt] = area  # 纪录岛屿面积
                cnt += 1
    
    res = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "0":
                max_island = 1  # 将水变为陆地，故从1开始计数
                v = set()
                for x, y in directions:
                    new_x = i + x
                    new_y = j + y
                    if (
                        0 <= new_x < len(grid)
                        and 0 <= new_y < len(grid[0])
                        and grid[new_x][new_y] != "0"
                        and grid[new_x][new_y] not in v  # 岛屿不可重复
                    ):
                        max_island += rec[grid[new_x][new_y]]
                        v.add(grid[new_x][new_y])
                res = max(res, max_island)

    if res == 0:
        return max(rec.values())  # 无水的情况
    return res
    
if __name__ == "__main__":
    print(main())