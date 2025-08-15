# s = input()
# s = '#'.join('^' + s + '$')
# curCenter = 0
# rightMost = 0
# arm = [0] * len(s)
# armMax = 0
# centerMax = 0

# for i in range(1, len(s)-1):
#     if i <= rightMost:
#         arm[i] = min(rightMost-i, arm[2*curCenter-i])
#     while s[i + arm[i] + 1] == s[i - arm[i]-1]:
#         arm[i] += 1
#     if i + arm[i] > rightMost:
#         rightMost = i + arm[i]
#         curCenter = i
#     if arm[i] > armMax:
#         armMax = arm[i]
#         centerMax = i

# print(armMax//2)



s = input()
res = []

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j] == s[i:j][::-1]:
            res.append(j-i)
if res:
    print(max(res))