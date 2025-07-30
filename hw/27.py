from collections import Counter

inputList = input().split()
n = int(inputList[0])
words = inputList[1:n+1]
s = inputList[n+1]
k = int(inputList[n+2])

sCnt = Counter(s)
res = []
for word in words:
    if Counter(word) == sCnt:
        res.append(word)
res.sort()
print(len(res))
if k < len(res):
    print(res[k])


