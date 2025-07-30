class Node:
    def __init__(self, val):
        self.val = val
        self.next = []
        self.inDegree = 0

    def follow(self, val):
        self.next.append(val)

def main():
    n, m = map(int, input().split())
    files = [ Node(_) for _ in range(n) ]
    for _ in range(m):
        prev, next = map(int, input().split())
        files[prev].follow(next)
        files[next].inDegree += 1

    que = []
    for file in files:
        if file.inDegree == 0:
            que.append(file)

    res = []
    while que:
        file = que.pop(0)
        res.append(file.val)
        for no in file.next:
            files[no].inDegree -= 1
            if files[no].inDegree == 0:
                que.append(files[no])
    if len(res) == n:
        print(*res)
    else:
        print(-1)

if __name__ == "__main__":
    main()