n, m, q = map(int, input().split())
from copy import deepcopy
dp = []
for i in range(n):
    s = input()
    dp.append([])
    for j in s:
        dp[i].append(int(j))
    


plans = []
for no in range(q):
    plans.append([])
    for i in range(n):
        s = input()
        line = []
        for j in s:
            line.append(int(j))
        plans[no].append(line)
        
visited = [False] * q
# 0 -> space
# 1 -> thing
# 2 -> space with light
# 3 -> thing with light
def light(photo, graph):
    for i in range(n):
        for j in range(m):
            if photo[i][j] == 0 and graph[i][j] == 1:
                photo[i][j] = 2
            if photo[i][j] == 1 and graph[i][j] == 1:
                photo[i][j] = 3


def check(photo):
    for i in range(n):
        for j in range(m):
            if photo[i][j] == 0 or photo[i][j] == 3:
                return False
    return True

res = []
def dfs(dp, start, pathLen):
    if check(dp):
        res.append(pathLen.copy())
        return 
    else:
        for no in range(start, q):
            if not visited[no]:
                visited[no] = True
                temp = deepcopy(dp)
                light(temp, plans[no])
                pathLen.append(no+1)
                dfs(temp, start+1, pathLen)
                visited[no] = False
                pathLen.pop()
        return

pathLen = []
dfs(dp, 0, pathLen)
if res:
    minLen = q + 1
    ans = None
    for p in res:
        if len(p) < minLen:
            minLen = len(p)
            ans = p
    print(minLen)
    print(*ans)
else:
    print(-1)




