n, h = map(int, input().split())
ques = []
for _ in range(n):
    ques.append(list(map(int, input().split())))


def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def solve(a,b,c):
    miror = [a, b, h * 2 - c]
    temp = miror.copy()
    while len(temp) > 1:
        num1 = temp.pop()
        num2 = temp.pop()
        temp.append(gcd(num1, num2))
    return [ it//temp[0] for it in miror]

for que in ques:
    ans = solve(*que)
    print(*ans)
    