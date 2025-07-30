s, t = input().split()
s += t
s = list(s)

def bubbleSort(s, start):
    for i in range(start, len(s), 2):
        swapFlag = False
        for j in range(start, len(s) -  i + start, 2):
            if j + 2 < len(s):
                if ord(s[j]) > ord(s[j+2]):
                    s[j], s[j+2] = s[j+2], s[j]
                    swapFlag = True
        if not swapFlag:
            return 

bubbleSort(s, 0)
bubbleSort(s, 1)

res = ''

for item in s:
    if item in '0123456789ABCDEFabcdef':
        binaryS = f'{bin(int(item, 16))[2:]:0>4}'
        binaryS = ''.join(reversed(binaryS))
        res += hex(int(binaryS, 2))[2:].upper()
    else:
        res += item

print(res)
