def valuableCase():
    n, caseV = (int(x) for x in input().split())
    weights, values = [], []
    for _ in range(n):
        a, b = (int(x) for x in input().split())
        weights.append(a)
        values.append(b)
    
    dp = [ 0 ] * (caseV + 1)
    
    for i in range(n):
        for j in range( weights[i], caseV+1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    print(dp[caseV]) 

if __name__ == "__main__":
    valuableCase()