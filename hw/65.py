small = input()
large = input()

if len(large) < len(small):
    small, large = large, small

dp = [ [0] * len(large) for _ in range(len(small))]

maxL = 0
maxSubString = ''


for i in range(len(small)-1, -1, -1):
    for j in range(len(large)-1, -1, -1):
        if i == len(small)-1 and small[-1] == large[j]:
            dp[i][j] = 1
        elif j == len(large)-1 and large[-1] == small[i]:
            dp[i][j] = 1
        elif small[i] == large[j]:
            dp[i][j] = dp[i+1][j+1] + 1
            if dp[i][j] >= maxL:
                maxL = dp[i][j]
                maxSubString = small[i:i+maxL]
        else:
            dp[i][j] = 0

print(maxSubString)
