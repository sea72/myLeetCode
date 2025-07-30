def findHighGround():
    n, m = map(int, input().split())
    grids = []
    for _ in range(n):
        grids.append(list(map(int, input().split())))
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    res = []

    

    def dfs(i, j, status, visited):
        if i == 0 or j == 0:
            status[0] = True    
        if i == n-1 or j == m-1:
            status[1] = True
        if status[0] and status[1]:
            return status
        visited[i][j] = True
        for addX, addY in directions:
            nextX, nextY = i + addX, j + addY
            if nextX < 0 or nextX > n-1 or nextY < 0 or nextY > m-1:
                continue
            if not visited[nextX][nextY] and grids[nextX][nextY] <= grids[i][j]:
                temp = dfs(nextX, nextY, status, visited)
                status = [status[0] or temp[0], status[1] or temp[1]]
                if status[0] and status[1]:
                    break
        return status
        

    for i in range(n):
        for j in range(m):
            visited = [ [False] * m for _ in range(n)]
            temp = dfs(i, j, [False, False], visited)
            if temp[0] and temp[1]:
                res.append((i, j))

    for line in res:
        print(' '.join(map(str, line)))

if __name__ == "__main__":
    findHighGround()