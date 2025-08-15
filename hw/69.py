x = int(input())
y = int(input())
z = int(input())

a = []
for _ in range(x):
    a.append(list(map(int, input().split())))

b = []
for _ in range(y):
    b.append(list(map(int, input().split())))

c = [ [0] * z for _ in range(x) ]

for i in range(x):
    for j in range(z):
        for k in range(y):
            c[i][j] += a[i][k] * b[k][j]

for line in c:
    print(*line)