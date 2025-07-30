# def cal():
#     rank = {
#         '+':0,
#         '-':0,
#         '*':1,
#         '/':1
#     }

#     def compute(opStack, numStack):
#         b = numStack.pop()
#         a = numStack.pop()
#         op = opStack.pop()
#         if op == '+':
#             a += b
#         elif op == "-":
#             a -= b
#         elif op == '*':
#             a *= b
#         elif op == '/':
#             a = int(a/b)
#         numStack.append(a)

#     s = input().translate(str.maketrans("{}[]", '()()'))
#     s = '(' + s + ')'
#     followingOpsFlag = False
#     opStack = []
#     numStack = []
#     i = 0
#     while i < len(s):
#         if s[i] == '(':
#             opStack.append(s[i])
#             i += 1
#         elif s[i] == ')':
#             while opStack[-1] != '(':
#                 compute(opStack, numStack)
#             opStack.pop()
#             i += 1
#         elif followingOpsFlag:
#             while opStack[-1] != '(' and rank[opStack[-1]] >= rank[s[i]]:
#                 compute(opStack, numStack)
#             opStack.append(s[i])
#             followingOpsFlag = False
#             i += 1
#         else:
#             cur = i
#             if s[i] ==  '-':
#                 i += 1
#             while s[i].isdigit():
#                 i += 1
#             numStack.append(int(s[cur:i]))
#             followingOpsFlag = True

#     print(numStack[-1])

# cal()


def cal2():
    s = input().translate(str.maketrans('{}[]', '()()'))
    rank = {
        '+':0,
        '-':0,
        '*':1,
        '/':1,
        '(':2
    }
    ops = []
    output = []
    followingNum = True
    i = 0
    while i < len(s):
        # check if op
        if s[i] in '+-*/(':
            # special negative num
            if followingNum and s[i] == '-':
                start = i
                i += 1
                while i < len(s) and s[i].isnumeric():
                    i += 1
                output.append(s[start:i])
                followingNum = False
            # sort on rank
            else:
                while ops and ops[-1] != '(' and rank[ops[-1]] >= rank[s[i]]:
                    op = ops.pop()
                    output.append(op)
                ops.append(s[i])
                i += 1
                followingNum = True
        # right column pop to left
        elif s[i] == ')':
            while ops:
                op = ops.pop()
                if op != '(':
                    output.append(op)
                else:
                    break
            i += 1
            followingNum = False
        # ordinary num
        else:
            start = i
            i += 1
            while i < len(s) and s[i].isnumeric():
                i += 1
            output.append(s[start:i])
            followingNum = False
    output.extend(ops[::-1])


    import operator
    stack = []
    nameToFun = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda x,y : int(x/y)
    }
    for i in output:
        if i.strip('-').isnumeric():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(nameToFun[i](a, b))
            
    print(stack[-1]) 

cal2()

            





