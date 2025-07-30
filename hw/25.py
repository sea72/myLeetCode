datas = list(map(int, input().split()))
dataN, datas = datas[0], datas[1:]

rules = list(map(int, input().split()))
ruleN, rules = rules[0], rules[1:]



rules = list(set(rules))
rules.sort()

from collections import defaultdict
dic = defaultdict(list)

def isIn(rule, data):
    return str(rule) in str(data)

for no, data in enumerate(datas, start=0):
    for rule in rules:
        if isIn(rule, data):
            dic[rule].append((no, data))

res = []
for rule in rules:
    if dic[rule]:
        res.extend([rule, len(dic[rule])]) 
        for temp in dic[rule]:
            res.extend(temp)
print(len(res), end=" ")
print(*res)
