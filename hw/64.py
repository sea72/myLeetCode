n = int(input())
cur = 1
upBound, downBound = 1, min(4, n)

def up():
    global cur
    global upBound
    global downBound

    if upBound < cur <= downBound:
        cur -= 1

    elif cur == upBound:
        if cur == 1:
            cur = n
            upBound, downBound = max(cur-3,1), cur
        else:
            cur -= 1
            upBound -= 1
            downBound -= 1
        

def down():
    global cur
    global upBound
    global downBound

    if upBound <= cur < downBound:
        cur += 1
    elif cur == downBound:
        if cur == n:
            cur = 1
            upBound, downBound = cur, min(cur+3, n)
        else:
            cur += 1
            upBound += 1
            downBound += 1

dos = input()
for do in dos:
    if do == 'U':
        up()
    else:
        down()
ans = list(range(upBound, downBound+1))
print(*ans)
print(cur)
