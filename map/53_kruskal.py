class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))

    def find(self, index):
        if self.ancestor[index] != index:
            self.ancestor[index]  = self.find(self.ancestor[index])
        return self.ancestor[index]

    def union(self, index1, index2):
        self.ancestor[self.find(index1)] = self.find(index2)

    def isSame(self, index1, index2):
        return self.find(index1) == self.find(index2)


def main():
    v, e = map(int, input().split())
    # graph = [[10001] * (v+1) for _ in range(v+1)]
    edges = []


    for _ in range(e):
        start, end, val = map(int, input().split())
        edges.append([start, end, val])
    edges.sort(key= lambda e: e[2])

    uf = UnionFind(10001)
    res = 0

    for i in range(v-1):
        start, end, val = edges[i]
        if uf.isSame(start, end):
            pass
        else:
            res += val
            uf.union(start, end)
    return res


if __name__ == "__main__":
    res = main()
    print(sum(res))

