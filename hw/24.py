
# n = int(input())
# heights = list(map(int, input().split(' ')))
# leftMostAscendingLength = [ 1 ] * n
# rightMostDescendingLength = [ 1 ] * n
# for cur in range(n):
#     for before in range(cur):
#         if heights[before] < heights[cur]:
#             leftMostAscendingLength[cur] = max(leftMostAscendingLength[before] + 1, leftMostAscendingLength[cur])
# for cur in range(n-1, -1, -1):
#     for after in range(n-1, cur, -1):
#         if heights[after] < heights[cur]:
#             rightMostDescendingLength[cur] = max(rightMostDescendingLength[cur], rightMostDescendingLength[after] + 1)

# ans = max( [ leftMostAscendingLength[i] + rightMostDescendingLength[i] for i in range(n)] ) - 1
# print(n - ans)



# import bisect
# def inc_max(l):
#     dp = [1]*len(l) # 初始化dp，最小递增子序列长度为1
#     arr = [l[0]] # 创建数组
#     for i in range(1,len(l)): # 从原序列第二个元素开始遍历
#         if l[i] > arr[-1]:
#             arr.append(l[i])
#             dp[i] = len(arr)
#         else:
#             pos = bisect.bisect_left(arr, l[i]) # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
#             arr[pos] = l[i]
#             dp[i] = pos+1
#     return dp
 
# while True:
#     try:
#         N = int(input())
#         s = list(map(int, input().split()))
#         left_s = inc_max(s) # 从左至右
#         right_s = inc_max(s[::-1])[::-1] # 从右至左
#         print(left_s, right_s)
#         sum_s = [left_s[i]+right_s[i]-1 for i in range(len(s))] # 相加并减去重复计算
#         print(str(N-max(sum_s)))
#     except:
#         break

import bisect 
n = int(input())
heights = list(map(int, input().split()))
def findMaxAscendingLength( heights):
    res = [ 1 ] * len(heights)
    dp = [ heights[0] ]
    for i in range(1, len(heights)):
        if heights[i] > dp[-1]:
            dp.append(heights[i])
            res[i] = len(dp)
        else:
            cur = bisect.bisect_left(dp, heights[i])
            dp[cur] = heights[i]
            res[i] = cur + 1
    return res

forward, backward = findMaxAscendingLength(heights), findMaxAscendingLength(heights[::-1])[::-1]
total = [ i + j for i, j in zip(forward, backward)]
print(n - max(total) + 1)


