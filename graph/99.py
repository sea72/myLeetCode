# def findIslands():
#     n, m = map(int, input().split())
#     graph = []
#     for i in range(n):
#         graph.append(list(map(int, input().split())))
#     visited = [[False] * m for _ in range(n)]
#     res = 0
#     dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
#     def dfs(i, j):
#         if i < 0 or i > n-1 or j < 0 or j > m-1 or visited[i][j]:
#             return
#         elif graph[i][j] and not visited[i][j]:
#             visited[i][j] = True
#             for addX, addY in dirs:
#                 dfs(i + addX, j + addY)

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] and not visited[i][j]:
#                 res += 1
#                 dfs(i, j)

#     print(res)

# if __name__ == "__main__":
#     findIslands()

from collections import deque
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(grid, visited, x, y):
    que = deque([])
    que.append([x,y])
    visited[x][y] = True
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in directions:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_y < 0 or next_x < 0 or next_x >= len(grid) or next_y >= len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y] == 1: 
                visited[next_x][next_y] = True
                que.append([next_x, next_y])


def main():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                res += 1
                bfs(grid, visited, i, j)
    print(res)

if __name__ == "__main__":
    main()

