from functools import reduce

def reachable():
    n, k = map(int, input().split())
    grids =[ [] for _ in range(n+1)]
    for _ in range(k):
        s, e = map(int, input().split())
        grids[s].append(e)
    visited = [False] * (n+1)
    myQue = [1]
    while myQue:
        cur = myQue.pop(0)
        for next in grids[cur]:
            if not visited[next]:
                visited[next] = True
                myQue.append(next)

    if reduce(lambda x,y : x & y, visited[2:]):
        print(1)
    else:
        print(-1)


if __name__ == "__main__":
    reachable()