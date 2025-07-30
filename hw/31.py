import re

string = input()
match = re.finditer(r'[A-Za-z]+', string)
res = [ i.group() for i in match]
res.sort()
print(*res)