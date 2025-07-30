s = input()
t = input()
dp = [ [None] * len(t) for _ in range(len(s))]

for j in range(len(t)):
    if s[0] in t[0:j+1]:
        dp[0][j] = j
    else:
        dp[0][j] = j+1

for i in range(len(s)):
    if t[0] in s[0:i+1]:
        dp[i][0] = i
    else:
        dp[i][0] = i + 1


for i in range(1, len(s)):
    for j in range(1, len(t)):
        if t[i] == s[j]:                                                                                                                                                                                                                                             
            dp[i][j] = dp[i-1][j-1] 
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

print(dp[-1][-1])




