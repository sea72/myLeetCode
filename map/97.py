# from math import inf

# def findPath():
#     n, m = map(int, input().split())
#     grids = [ [ [inf] * (n+1) for _ in range(n+1)]  for _ in range(n+1)]
#     for _ in range(m):
#         u, v, w = map(int, input().split())
#         grids[u][v][0] = w
#         grids[v][u][0] = w
#     q = int(input())
#     plans = []
#     for _ in range(q):
#         s, e = map(int, input().split())
#         plans.append([s, e])
    
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 grids[i][j][k] = min(grids[i][j][k-1], grids[i][k][k-1] + grids[k][j][k-1])
    
#     for s, e in plans:
#         if grids[s][e][n] < inf:
#             print(grids[s][e][n])
#         else:
#             print(-1)


# findPath()



# from math import inf

# def findPath():
#     n, m = map(int, input().split())
#     grids = [ [inf] * (n+1) for _ in range(n+1)]
#     for _ in range(m):
#         u, v, w = map(int, input().split())
#         grids[u][v] = w
#         grids[v][u] = w
#     q = int(input())
#     plans = []
#     for _ in range(q):
#         s, e = map(int, input().split())
#         plans.append([s, e])
    
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 grids[i][j] = min(grids[i][j], grids[i][k] + grids[k][j])
    
#     for s, e in plans:
#         if grids[s][e] < inf:
#             print(grids[s][e])
#         else:
#             print(-1)


# findPath()


