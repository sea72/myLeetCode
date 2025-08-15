from functools import cache

@cache
def triangle(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1, 1]
    else:
        upper = [0, 0] + triangle(n-1) + [0, 0]
        res = []
        for i in range(1, len(upper)-1):
            res.append(upper[i-1] + upper[i] + upper[i+1])
    return res

i = int(input())
for no, v in enumerate(triangle(i), 1):
    if v & 1 == 0:
        print(no)
        break
else: 
    print(-1)