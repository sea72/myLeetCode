# def perimeter():
#     n, m = map(int, input().split())
#     grids = []
#     for _ in range(n):
#         grids.append(list(map(int, input().split())))

#     leftUp = [[-1, 0], [0, -1]]
#     rightDown = [[1, 0], [0, 1]]
#     visited = [ [False] * m for _ in range(n)]
#     neighbor = 0
#     island = 0


    
#     def dfs(i, j):
#         nonlocal island
#         nonlocal neighbor
#         visited[i][j] = True
#         island += 1
#         for dx, dy in leftUp:
#             nx, ny = i + dx, j + dy
#             if  0 <= nx <= n - 1 and 0 <= ny <= m-1 and not visited[nx][ny] and grids[nx][ny] == 1 :
#                 dfs(nx, ny)
#         for dx, dy in rightDown:
#             nx, ny = i + dx, j + dy
#             if  0 <= nx <= n - 1 and 0 <= ny <= m-1:
#                 if grids[nx][ny] == 1 :
#                     neighbor += 1
#                     if not visited[nx][ny]:
#                         dfs(nx, ny)
    
#     for i in range(n):
#         for j in range(m):
#             if not visited[i][j] and grids[i][j]:
#                 dfs(i, j)
    
#     print(island * 4 - neighbor * 2)


# if __name__ == "__main__":
#     perimeter()



def perimeter():
    n, m = map(int, input().split())
    grids = []
    for _ in range(n):
        grids.append(list(map(int, input().split())))

    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    visited = [ [False] * m for _ in range(n)]
    edge = 0
      
    def dfs(i, j):
        nonlocal edge
        visited[i][j] = True
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if nx in (-1, n) or ny in (-1, m):
                edge += 1
            if 0 <= nx <= n - 1 and 0 <= ny <= m-1:
                if grids[nx][ny] == 0:
                    edge += 1
                if not visited and grids[nx][ny] == 1:
                    dfs(nx, ny) 
        
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grids[i][j]:
                dfs(i, j)
    
    print(edge)


if __name__ == "__main__":
    perimeter()