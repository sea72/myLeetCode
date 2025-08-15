n = int(input())
arrays = []
for _ in range(n):
    a,b = input().split()
    temp = a + ' ' + b
    arrays.append(temp)

dic = dict(zip( ( chr(no) for no in range(65, 98)), arrays  ))


inputStr = input()
calStack = []
res = 0

for i in inputStr:
    if i == ")":
        latterName = calStack.pop()
        fronterName = calStack.pop()
        fronter, latter = dic[fronterName], dic[latterName]
        a, b = list(map(int, fronter.split()))
        b, c = list(map(int, latter.split()))
        res += a * b * c
        calStack.pop()
        calStack.append(fronterName)
        dic[fronterName] = str(a) + ' ' + str(c)
    else:
        calStack.append(i)

print(res)


    

