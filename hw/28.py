from functools import cache

@cache
def isPrime(n):
    if n <= 3:
        return n > 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def match(odd):
    for i in range(len(evens)):
        if not mated[i] and isPrime(odd + evens[i]):
            # 虚线匹配
            mated[i] = True

            # 当什么情况做实线匹配
            if itsOdd[i] == 0 or match(itsOdd[i]):
                itsOdd[i] = odd
                return True
    return False

n = int(input())
nums = list(map(int, input().split()))
odds, evens = [], []
for num in nums:
    if num & 1 :
        odds.append(num)
    else:
        evens.append(num)

itsOdd = [0] * len(evens)
res = 0
for num in odds:
    mated = [False] * len(evens)
    if match(num):
        res += 1

print(res)

