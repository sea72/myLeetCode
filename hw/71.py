# while True:
#     s = input()
#     p = input()
#     upBound = [0] * len(p)


#     cur = 0
#     while cur < len(p):
#         start = cur
#         while cur < len(p) and p[cur].isalnum():
#             cur += 1
#         for temp in range(start, cur):
#             upBound[temp] = cur - 1
#         if cur < len(p):
#             upBound[cur] = cur
#         cur += 1

#     # left point to left bound waiting for match
#     # right point to right bound waiting for match
#     left, right = 0, 0

#     pointS = 0
#     while pointS < len(s) and left < len(p):
#         if s[pointS] == '*':
#             if p[left].isalnum():
#                 right = upBound[left] + 1
#                 pointS += 1
#             else:
#                 break
#         elif s[pointS] == '?':
#             if p[left].isalnum():
#                 right = upBound[left] + 1 
#                 left += 1
#                 pointS += 1
#             else:
#                 break
#         elif s[pointS].isalpha():
#             while left <= right:
#                 if p[left] not in (s[pointS].lower(), s[pointS].upper()):
#                     left += 1
#                 else:
#                     left += 1
#                     right = max(left, right)
#                     pointS += 1
#                     break
#             else:
#                 break
#         else:
#             while left <= right:
#                 if p[left] != s[pointS]:
#                     left += 1
#                 else:
#                     left += 1
#                     right = max(left, right)
#                     pointS += 1
#                     break
#             else:
#                 break

#     if pointS == len(s) and (right == len(p) or left == len(p)) :
#         print('true')
#     else:
#         print('false')




def do():
    p = input()
    s = input()

    m, n = len(p), len(s)

    i, j = 0, 0 
    iRecord, jRecord = -1, -1

    def isSame(a: str, b:str):
        if a.isalpha() and b.isalpha():
            return a.lower() == b.lower()
        elif a.isdigit() and b.isdigit():
            return a == b
        elif a =='?' and b.isalnum():
            return True
        else:
            return a == b


    while j < n:
        if i < m and isSame(p[i], s[j]):
            i += 1
            j += 1
        elif i < m and p[i] == '*':
                iRecord = i
                jRecord = j
                i += 1
        elif jRecord >= 0:
            jRecord += 1
            j = jRecord
            i = iRecord + 1
        else:
            return False
    
    while i < m and p[i] == '*':
        i += 1
    return i == m

    

while True:
    if do():
        print('true')
    else:
        print('false')


