def main():
    c, n = map(int, input().split())
    weights = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    volumes = list(map(int, input().split()))
    # c, n = 10,3
    # weights = [1,3,4]
    # prices = [15,20,30]
    # volumes = [2,3,2]
    newWeights = []
    newPrices = []
    for i in range(len(volumes)):
        newWeights.extend([ weights[i] for _ in range(volumes[i])])
    for i in range(len(volumes)):
        newPrices.extend([ prices[i] for _ in range(volumes[i])])
    dp = [0] * (c+1)
    for i in range(sum(volumes)):
        for j in range(c, 0, -1):
            if j >= newWeights[i]:
                dp[j] = max(dp[j - newWeights[i]] + newPrices[i] , dp[j]) 
    print(dp[c])

def main2():
    c, n = map(int, input().split())
    weights = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    volumes = list(map(int, input().split()))

    dp = [0] * (c+1)

    for i in range(n):
        for j in range(c, 0, -1):
            for k in range(1, volumes[i] + 1):
                if j < k * weights[i]:
                    break
                dp[j] = max(dp[j - k * weights[i]] + k * prices[i], dp[j])

    print(dp[c])
    
main2()



