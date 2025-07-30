# 第一行包含两个正整数，第一个整数 M 代表研究材料的种类，第二个正整数 N，代表小明的行李空间。
# 第二行包含 M 个正整数，代表每种研究材料的所占空间。 
# 第三行包含 M 个正整数，代表每种研究材料的价值



# def valuableCase():

#     space = int(input().split()[1])
#     spaces = list(map(int, input().split()))
#     values = list(map(int, input().split()))
#     n = len(spaces)
#     maxValue = 0

#     def traverse(no, tempValue, tempRemainSpace):
#         if no == n:
#             nonlocal maxValue
#             maxValue = max(maxValue, tempValue)
#         else:
#             if tempRemainSpace >= spaces[no]:
#                 traverse(no+1, tempValue + values[no], tempRemainSpace - spaces[no])
#             traverse(no+1, tempValue, tempRemainSpace)

#     traverse(0, 0, space)
#     print(maxValue)

def valuableCase():
    n = list(map(int, input().split()))
    weight = list(map(int, input().split()))    
    vals = list(map(int, input().split()))
    # n = [6,1]
    # weight = [2, 2, 3, 1, 5, 2]
    # vals = [2, 3, 1, 5, 4, 3]
    nums, bagVolume = n[0], n[1]
    dp = [[0] * (bagVolume + 1) for _ in range(nums + 1)]
    
    for i in range(1, nums + 1):
        for j in range(1, bagVolume + 1):
            if j >= weight[i-1]:
                dp[i][j] = max(dp[i-1][j-weight[i-1]] + vals[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[nums][bagVolume])


def valuableCase():
    # input 
    n = list(map(int, input().split()))
    weight = list(map(int, input().split()))    
    vals = list(map(int, input().split()))
    nums, bagVolume = n[0], n[1]
    # n = [6,1]
    # weight = [2, 2, 3, 1, 5, 2]
    # vals = [2, 3, 1, 5, 4, 3]
    
    dp = [0] * (bagVolume + 1)

    for i in range(1, nums+1):
        for j in range(bagVolume, 0, -1):
            if j >= weight[i-1]:
                dp[j] = max(dp[j], dp[j-weight[i-1]] + vals[i-1])
    print(dp[bagVolume])





    dp = [[0] * (bagVolume + 1) for _ in range(nums + 1)]
    
    for i in range(1, nums + 1):
        for j in range(1, bagVolume + 1):
            if j >= weight[i-1]:
                dp[i][j] = max(dp[i-1][j-weight[i-1]] + vals[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[nums][bagVolume])


    
if __name__ == '__main__':
    valuableCase()


