from math import inf

def findPath():
    n, m = map(int, input().split())
    grids = [ [inf] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        grids[u][v] = w


    paths = [ [-1] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            grids[i][i] = 0
            if grids[i][j] != inf:
                paths[i][j] = i
            paths[i][i] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                paths[i][j] = paths[k][j] if grids[i][j] > grids[i][k] + grids[k][j] else paths[i][j]
                grids[i][j] = min(grids[i][j], grids[i][k] + grids[k][j])

                # you must modify paths before you assigh new value to grids
                # when k-road and orginal-road are equal, change or not ?
                # eg i,j,k = 1, 3, 3, means 1 -> 3 add minpoint 1->3->3
                # they're equals,but paths[3][3] = -1, you should avoid change 1->3' path to -1
                # so you stay path[1][3], which means when equals, don't change path[i][j]

    print('plese check')
    while True:
        s, e = map(int, input().split())
        if grids[s][e] < inf:
            print(grids[s][e])
            temp = []
            while s!= e:
                temp.append(e)
                e = paths[s][e]
            print([e] + temp[::-1])
        else:
            print(-1)

findPath()