n = int(input())
weights = list(map(int, input().split()))
numbers = list(map(int, input().split()))

canWeights = {0}
for i in range(n):
    for j in range(numbers[i]):
        for canWeight in list(canWeights):
            canWeights.add(canWeight + weights[i])

print(len(canWeights))
