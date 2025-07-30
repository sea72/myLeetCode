# from math import inf

# def findPath():
#     n, m = map(int, input().split())
#     paths = [ [] for _ in range(n+1)]
#     for _ in range(m):
#         s, e, v = map(int, input().split())
#         paths[s].append((e, v))
#     res = []
    
#     def dfs(cur, val):
#         if cur == n:
#             res.append(val)
#             return
#         if not paths[cur]:
#             return
#         for next, expense in paths[cur]:
#             dfs(next, val + expense)
        
#     dfs(1, 0)
#     if res:
#         print(min(res))
#     else:
#         print(-1)


# def findPath2():
#     n, m = map(int, input().split())
#     paths = [ [] for _ in range(n+1)]
#     minDist = [ inf ] * (n+1)
#     visited = [ False ] * (n+1)
#     for _ in range(m):
#         s, e, v = map(int, input().split())
#         paths[s].append((e, v))
    
#     minDist[1] = 0

#     for i in range(1, n+1):
#         minVal = inf
#         cur = 1

#         for vertex in range(1, n+1):
#             if not visited[vertex] and minDist[vertex] < minVal:
#                 minVal = minDist[vertex]
#                 cur = vertex
        
#         visited[cur] = True

#         for vertex in range(1, n+1):
#             if not visited[vertex] and paths[cur]:
#                 for next, expense in paths[cur]:
#                     if next == vertex and minDist[vertex] > minDist[cur] + expense:
#                         minDist[vertex] = minDist[cur] + expense

#         print(minDist)

#     if minDist[n] == inf:
#         print(-1)
#     else:
#         print(minDist[n])

# if __name__ == "__main__":
#     findPath2()



import heapq

class Edge:
    def __init__(self, to, val):
        self.to = to
        self.val = val

def dijkstra(n, m, edges, start, end):
    grid = [[] for _ in range(n + 1)]

    for p1, p2, val in edges:
        grid[p1].append(Edge(p2, val))

    minDist = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    pq = []
    heapq.heappush(pq, (0, start))
    minDist[start] = 0

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if visited[cur_node]:
            continue

        visited[cur_node] = True

        for edge in grid[cur_node]:
            if not visited[edge.to] and cur_dist + edge.val < minDist[edge.to]:
                minDist[edge.to] = cur_dist + edge.val
                heapq.heappush(pq, (minDist[edge.to], edge.to))

    return -1 if minDist[end] == float('inf') else minDist[end]

# 输入
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start = 1  # 起点
end = n    # 终点

# 运行算法并输出结果
result = dijkstra(n, m, edges, start, end)
print(result)



    
