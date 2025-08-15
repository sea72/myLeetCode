n = int(input())


primes = []
for i in range(2, 1001):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        primes.append(i)

primesDict = dict(zip(primes, range(len(primes))))

low, high = 0, len(primes)
while low <= high:
    mid = (low + high) // 2
    if primes[mid] >= n/2 :
        high = mid-1
    else:
        low = mid+1
cur = low
for i in range(cur, 1001):
    if n - primes[i] in primesDict.keys():
        print(n - primes[i], primes[i], sep='\n')
        break
else:
    print(-1)