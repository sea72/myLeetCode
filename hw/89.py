# from operator import add, sub, mul
# from itertools import permutations


# cards = ['A', '2', '3','4','5','6','7','8','9','10','J','Q','K']
# dic = dict(zip(cards, range(1, len(cards)+1)))
# reverseDic = dict(zip(range(1, len(cards)+1), cards))


# nameToFun = {
#     '+': add,
#     '-': sub,
#     '*': mul,
#     '/': lambda x,y : int(x//y)
# }
# rank = {
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2
# }

# def cal(nums):
#     for op1 in '+-*/':
#         for op2 in '+-*/':
#             for op3 in '+-*/':
#                 try:
#                     ops = [op1, op2, op3]
#                     temp = nums.copy()
#                     while ops:
#                         a = temp.pop()
#                         b = temp.pop()
#                         curOp = ops.pop()
#                         if ops and rank[curOp] < rank[ops[-1]]:
#                             nextOp = ops.pop()
#                             c = temp.pop()
#                             temp.append(nameToFun[nextOp](b, c))
#                             temp.append(a)
#                             ops.append(curOp)
#                         else:
#                             temp.append(nameToFun[curOp](a, b))
#                     if temp[-1] == 24:
#                         res = f'{reverseDic[nums[-1]]}{op3}{reverseDic[nums[-2]]}{op2}{reverseDic[nums[-3]]}{op1}{reverseDic[nums[-4]]}'
#                         return res
#                 except ZeroDivisionError:
#                     pass
#     return None

# s = input().split()
# if 'joker' in s or 'JOKER' in s:
#     print('ERROR')
# else:
#     nums = [dic[_] for _ in s]
#     allNum = permutations(nums)
#     for nums in allNum:
#         res = cal(list(nums))
#         if res:
#             print(res)
#             break
#     else:
#         print('NONE')


from operator import add, sub, mul
from itertools import permutations


cards = ['A', '2', '3','4','5','6','7','8','9','10','J','Q','K']
dic = dict(zip(cards, range(1, len(cards)+1)))
reverseDic = dict(zip(range(1, len(cards)+1), cards))


nameToFun = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': lambda x,y : int(x//y)
}
rank = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def cal(nums):
    for op1 in '+-*/':
        for op2 in '+-*/':
            for op3 in '+-*/':
                try:
                    ops = [op1, op2, op3]
                    temp = nums.copy()
                    while ops:
                        a = temp.pop()
                        b = temp.pop()
                        curOp = ops.pop()
                        temp.append(nameToFun[curOp](a, b))
                    if temp[-1] == 24:
                        res = f'{reverseDic[nums[-1]]}{op3}{reverseDic[nums[-2]]}{op2}{reverseDic[nums[-3]]}{op1}{reverseDic[nums[-4]]}'
                        return res
                except ZeroDivisionError:
                    pass
    return None

s = input().split()
if 'joker' in s or 'JOKER' in s:
    print('ERROR')
else:
    nums = [dic[_] for _ in s]
    allNum = permutations(nums)
    for nums in allNum:
        res = cal(list(nums))
        if res:
            print(res)
            break
    else:
        print('NONE')
