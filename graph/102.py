def sinkIsland():
    # input
    n, m = map(int, input().split())
    grids = []
    for _ in range(n):
        grids.append(list(map(int, input().split())))

    # introduce necessary variate
    visited = [ [False] * m for _ in range(n)]
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    temp = []
    isLone = True
    
    # dfs
    def dfs(i, j):
        nonlocal isLone
        temp.append([i,j])
        visited[i][j] = True
        if i in (0, n-1) or j in (0, m-1):
            isLone = False
        for addX, addY in directions:
            nextX, nextY = i + addX, j + addY
            if nextX < 0 or nextX > n - 1 or nextY < 0 or nextY > m - 1:
                continue
            elif grids[nextX][nextY] and not visited[nextX][nextY]:
                dfs(nextX, nextY)


    for i in range(n):
        for j in range(m):
            if grids[i][j] and not visited[i][j]:
                temp = []
                isLone = True
                dfs(i, j)
                if isLone:
                    for x, y in temp:
                        grids[x][y] = 0
    
    for line in grids:
        print(*line)


if __name__ == "__main__":
    sinkIsland()