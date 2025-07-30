from collections import Counter

counter = Counter()

n = int(input())

for _ in range(n):
    k, v = map(int, input().split())
    counter[k] += v

res = sorted(counter.items(), key= lambda e:e[0])
for temp in res:
    print(*temp)

