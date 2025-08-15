# 暴力算法，能拿一半的分
# a, b = map(int, input().split('/'))
# lst = [i for i in range(2, 201)]

# def dfs(remain, nums):
#     if remain < 1e-7:
#         return nums
#     elif len(nums) >= 5:
#         return
#     else:
#         for n in lst:
#             if remain > 1/n:
#                 ans = dfs(remain - 1/n, nums + [n])
#                 if ans:
#                     return ans
#     return None

# ans = dfs(a/b, [])
# if ans:
#     ans = [ f'1/{i}'for i in ans]
#     print('+'.join(ans))


# def allmod(i):
#     temp = []
#     for j in range(2, i):
#         if i % j == 0:
#             temp.append(j)
#     return  temp[::-1] + [1]

# def dfs(remain, temp, ans):
#     if remain == 0:
#         return ans
#     for no in range(len(temp)):
#         if temp[no] <= remain:
#             res = dfs(remain - temp[no], temp[:no] + temp[no+1:], ans+[temp[no]])
#             if res:
#                 return res
#     return None


# a, b = map(int, input().split('/'))
# for i in range(1, 11):
#     down = b * i
#     temp = allmod(down)
#     res =  dfs(a*i, temp, [])
#     if res:
#         if len(res) == 1:
#             print(f'1/{b//res[-1]}')
#         else:
#             ss = [f'1/{iiii}' for iiii in res]  # 思路对一点，但是这里返回的是约数，而不是分母，还要转换一次
#             print('+'.join(ss))
#         break

# def fun(n,m):
#     if n == 1:
#         res.append(m)
#         return res
#     if m % n == 0:
#         res.append(m // n)
#         return res
#     while n > 1:
#         k = m // n + 1
#         res.append(k)
#         return fun(n * k - m, m * k)

# while True:
#     try:
#         n, m = map(int, input().split('/'))
#         res = []
#         result = fun(n, m)
#         print('1/' + '+1/'.join(map(str, result)))
#     except:
#         break

while True:
    try:
        a, b = map(int, input().split('/'))
        a *= 10
        b *= 10
        res = []
        while a:
            for i in range(a, 0, -1):
                if b % i == 0:
                    res.append(f'1/{int(b/i)}')
                    a -= i
                    break
        print('+'.join(res))
    except:
        break






