def find(i):
    temp = [1]
    for j in range(2, i):
        if i % j == 0:
            temp.append(j)
    return sum(temp) == i

ans = 0
n = int(input())
for i in range(2, n+1):
    if find(i):
        ans += 1
print(ans)

    
