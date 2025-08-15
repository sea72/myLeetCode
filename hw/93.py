n = int(input())
nums = list(map(int, input().split()))


def f(nums, aim):
    if not nums and aim == 0:
        return True

    minSum = sum(x for x in nums if x < 0)
    maxSum = sum(x for x in nums if x > 0)
    offset = -minSum
    
    x = len(nums)
    y = maxSum - minSum + 1
    dp = [ [False] * y for _ in range(x)]

    for i in range(x):
        dp[i][offset] = True

    for i in range(x):
        for j in range(y):
            # if j >= nums[i]:
            #     dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
            # else:
            #     dp[i][j] = dp[i-1][j]
            if 0 <= j - nums[i] < y:
                dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
            
    
    return dp[-1][aim+offset]



a, b, c = [], [], []
for n in nums:
    if n % 5 == 0:
        a.append(n)
    elif n % 3 == 0:
        b.append(n)
    else:
        c.append(n)





aim = sum(nums)
if aim & 1 == 1:
    print('false')

else:
    if f(c, aim//2 - sum(a)):
        print('true')
    else:
        print('false')
    

    
