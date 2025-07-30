pw = input()
dic = dict(zip('abcdefghijklmnopqrstuvwxyz', [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]))
newPw = ''
for s in pw:
    if s.isupper():
        newPw += chr(ord(s) + 33) if s != "Z" else 'a'
    elif s.islower():
        newPw += str(dic[s])
    else:
        newPw += s
print(newPw)
