# from itertools import accumulate

# n = input()
# lst = list(map(int, input().split()))
# temp = list(accumulate(lst))
# total = sum(lst)
# if total % 3 != 0:
#     print(0)
# else:
#     aimPrev = total // 3
#     aimNext = aimPrev * 2
#     res = 0
#     prev, next = -1, -1
#     flagPrev = False
#     flagNext = False
#     while prev < len(temp):
#         if temp[prev] > 0:
#             flagPrev = True
#         if temp[prev] == aimPrev and flagPrev:
#             next = prev + 1
#             flagNext = False
#             while next < len(temp):
#                 if temp[next] > 0:
#                     flagNext = True
#                 if temp[next] == aimNext and flagNext:
#                     res += 1
#                 next += 1
#         prev += 1

#     print(res)



# from itertools import accumulate

# n = input()
# lst = list(map(int, input().split()))
# temp = list(accumulate(lst))
# total = sum(lst)

# def dfs(start, end, times):
#     if start == len(lst) and times == 3:
#         global res
#         res += 1
#         return 
#     flag = False
#     for i in range(start, end+1):
#         if lst[i] > 0:
#             flag = True
#         if flag and temp[i] == aim * (times + 1):
#             dfs(i+1, end, times+1)

# if total % 3 != 0:
#     print(0)
# else:
#     aim = total // 3
#     times = 0
#     res = 0
#     dfs(0, len(lst)-1, times)
#     print(res)



# from itertools import accumulate

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     total = sum(a)
#     if total % 3 != 0:
#         print(0)
#         return
#     m = total // 3
#     pre = [0] * n
#     f = [0] * n
#     last = -1
#     freq = [0] * (n + 1)  
#     for i in range(n):
#         pre[i] = pre[i - 1] + a[i]
#         f[i] = f[i - 1] + (a[i] > 0)
#         if a[i] > 0:last = i
#         if pre[i] == m and f[i]:
#             freq[f[i]] += 1

#     g = list(accumulate(freq))
#     res = 0
#     for i in range(1, last + 1):
#         if pre[i - 1] == 2 * m:
#             x = f[i - 1] - 1
#             if x >= 0:
#                 res += g[x]
#     print(res)
# solve()



# from itertools import accumulate

# n = input()
# lst = list(map(int, input().split()))
# tempSum = list(accumulate(lst))
# postives = list(accumulate( [ i > 0  for i in lst ] ))
# total = sum(lst)
# if total % 3 != 0:
#     print(0)
# else:
#     aim = total // 3
#     res = 0
#     aimPos = []
#     aimDoublePos = []
#     for no in range(len(tempSum)):
#         if tempSum[no] == aim:
#             aimPos.append(no)
#         if tempSum[no] == aim * 2:
#             aimDoublePos.append(no)
    
#     for i in aimPos:
#         for j in aimDoublePos:
#             if i < j and postives[i] < postives[j]:
#                 res += 1

#     print(res)



from itertools import accumulate

n = int(input())
lst = list(map(int, input().split()))
tempSum = list(accumulate(lst))
positives = list(accumulate([int(i > 0) for i in lst]))
total = sum(lst)

if total % 3 != 0:
    print(0)
else:
    aim = total // 3
    # count_by_pos[k] 表征当正数个数为K个时，累计有多少个满足前缀和为m的位置
    
    # 因为postives一定是随下标单调递增的，故而其隐含了先后的顺序
    # 所以我们不用再用一个双循环，而是用一个count_by_pos数组来做一个统计
    # 长度为n的数组最多n个正数，再加一个0的情况，所以长度为n+1
    countTargetByPostives = [0] * (n + 1) 


    # 统计每个 前缀和为m 位置的正数个数（累加）
    for idx in range(n):
        if tempSum[idx] == aim:
            countTargetByPostives[positives[idx]] += 1

    # 把每个位置有几个，转变为累计有几个，方便计算
    countTargetByPostives[0] = 0
    prefixCount = list(accumulate(countTargetByPostives))


   
    res = 0
    for idx in range(1, n):
        if tempSum[idx] == aim * 2:
            # x = 正数个数 - 1，因为第二段至少 1 个正数
            # x为第一段最多有几个正数，因为正数的个数随下标递增，所以隐含了第一段最右能到什么位置
            x = positives[idx] - 1
            if x > 0 and positives[idx] < positives[-1]:
                res += prefixCount[x]
    print(res)
