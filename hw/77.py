n = int(input())
waitingIn = list(map(int, input().split()))[::-1]
waitngOut = []

res = []


def recurve(waitingIn, waitingOut, leave):
    if len(leave) == n:
        res.append(leave.copy())
    else:
        if waitingIn:
            i = waitingIn.pop()
            waitingOut.append(i)
            recurve(waitingIn, waitngOut, leave)
            waitingOut.pop()
            waitingIn.append(i)
        if waitingOut:
            i = waitingOut.pop()
            leave.append(i)
            recurve(waitingIn, waitngOut, leave)
            leave.pop()
            waitingOut.append(i)


recurve(waitingIn, waitngOut, [])
res.sort()
for it in res:
    print(*it)