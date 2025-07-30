import sys
from collections import Counter
from collections import deque

errShown = []
errQue = deque([])
errCnt = Counter()

for line in sys.stdin:
    inputStr = line.strip('\n').split(" ")
    if len(inputStr) == 2:
        fileName, lineNum = inputStr[0].split("\\")[-1], inputStr[1]
        if len(fileName) > 16:
            fileName = fileName[-16:]
        err = fileName + ' ' + lineNum
        if err not in errShown:
            errShown.append(err)
            errQue.append(err)
            errCnt[err] += 1
        else:
            errCnt[err] += 1
cnt = 8
res = []
while cnt and errQue:
    err = errQue.pop()
    res.append(f"{err} {errCnt[err]}")
    cnt -= 1

for s in res[::-1]:
    print(s)