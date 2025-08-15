# def findNum(lst, aim):
#     if not lst:
#         return False
#     if len(lst) == 1:
#         return lst[0]-aim < 1e-6
#     else:
#         for i in range(len(lst)):
#             newLst = lst[:i] + lst[i+1:]
#             opNum = lst[i]
#             if findNum(newLst, aim+opNum) or findNum(newLst, aim-opNum) or findNum(newLst, aim*opNum) or findNum(newLst, aim/opNum):
#                 return True
#         return False
    
# lst = list(map(int, input().split()))
# if findNum(lst, 24):
#     print('true')
# else:
#     print('false')



# def dfs(nums):
#     if not nums:
#         return False
#     if len(nums) == 1:
#         return abs(nums[0] - 24) < 1e-6
#     for i, a in enumerate(nums):                   # 获取第一个数字
#         for j, b in enumerate(nums):               # 获取第二个数字
#             if i != j:                             # 控制不重复
#                 newNums = list()
#                 for k, c in enumerate(nums):       # 获取第三个数字
#                     if k != i and k != j:
#                         newNums.append(c)
#                 for k in range(4):
#                     if k < 2 and i > j:            # 对于+和*操作来说不需要考虑两者的顺序，因此舍去一种
#                         continue
#                     if k == 0:
#                         newNums.append(a+b)
#                     if k == 1:
#                         newNums.append(a*b)
#                     if k == 2:
#                         newNums.append(a-b)
#                     if k == 3:
#                         if abs(b) < 1e-6:          # 排除除数为0的情况
#                             continue
#                         newNums.append(a/b)
#                     if dfs(newNums):
#                         return True
#                     newNums.pop()
#     return False

# while True:
#     try:
#         lst = [int(x) for x in input().split()]
#         if dfs(lst):
#             print('true')
#         else:
#             print('false')
#     except:
#         break



# def dfs(nums)



# def findNum(lst, aim):
#     '''
#     这种方法无法处理一颗2层的满二叉树，因为其通过运算产生了中间数，
#     我们通过24倒推时，每次仅处理了一位数字，所有运算都是通过与已存在的运算数一步运算而来
#     正确的逆波兰式子有5种结构
#     '''
#     if not lst:
#         return False
#     if len(lst) == 1:
#         return abs(lst[0] - aim) < 1e-6
#     else:
#         for i in range(len(lst)):
#             newLst = lst[:i] + lst[i+1:]
#             opNum = lst[i]
#             if aim != 0 and (findNum(newLst, aim+opNum) or findNum(newLst, aim-opNum) or findNum(newLst, opNum-aim) \
#                              or findNum(newLst, aim*opNum) or findNum(newLst, opNum/aim)):
#                 return True
#             elif opNum != 0 and (findNum(newLst, aim+opNum) or findNum(newLst, aim-opNum) or findNum(newLst, opNum-aim) \
#                             or findNum(newLst, aim*opNum) or findNum(newLst, aim/opNum)):
#                 return True
#             elif aim!=0 and opNum!=0 and (findNum(newLst, aim+opNum) or findNum(newLst, aim-opNum) or findNum(newLst, opNum-aim) or findNum(newLst, aim*opNum) or findNum(newLst, aim/opNum) or findNum(newLst, opNum/aim)):
#                 return True
#         return False

# lst = list(map(int, input().split()))
# if findNum(lst, 24):
#     print('true')
# else:
#     print('false')


def judgePoint24(nums):
    '''
    为什么正向遍历就能避免这个问题呢？
    
    在逆波兰的求解中，我们每次都是取两个数计算后放回，总是无限地重复了这一操作
    尽管存在(ab) (cd)这样的分组计算结果，但我们将第一步计算的结果插入到数组中
    然后通过遍历所有抽取情况，这时候下一步包含了ab, cd 这种分类计算结果，因为你上一步计算的结果
    并不一定在下一轮抽中，这就避免了那棵2层满二叉树没有得到计算的特列
         +
        / \ 
        *  * 
       /\  /\
       a b c d   


    其次，精度要加绝对值
    ''' 
    EPSILON = 1e-6  # 浮点精度容忍
    if len(nums) == 1:
        return abs(nums[0] - 24) < EPSILON

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                a, b = nums[i], nums[j]
                # 加减乘除
                candidates = [a + b, a - b, b - a, a * b]
                if b != 0:
                    candidates.append(a / b)
                if a != 0:
                    candidates.append(b / a)

                for c in candidates:
                    if judgePoint24(rest + [c]):
                        return True
    return False

lst = list(map(int, input("Enter four numbers: ").split()))
if judgePoint24(lst):
    print('true')
else:
    print('false')
