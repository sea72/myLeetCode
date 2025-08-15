# # 此法无法避免地处理掉了引号内的空格

# myList = input().split()
# myNewList = []
# watings = 0
# for item in myList:
#     temp = item.count('"')
#     if watings & 1 == 0:
#         myNewList.append(item.strip('"'))
#     elif watings & 1 == 1:
#         myNewList[-1] += item.strip('"')
#     watings += temp

# print(len(myNewList))
# for line in myNewList:
#     print(line)


s = input()
myList = [""]
continueFlag = False
spaceFlag = False
for char in s:
    if char == '"':
        continueFlag = not continueFlag
        continue
    if not continueFlag and char.isspace():
        myList.append("")
    else:
        myList[-1] += char

print(len(myList))

for line in myList:
    print(line)

    




