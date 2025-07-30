# import math
# n = int(input())
# for i in range(2, int(math.sqrt(n))+1):
#     while n % i == 0:
#         print(i, end=' ')
#         n = n // i
# if n > 2:
#     print(n)

# lst = []
# for i in range(2, 1000):
#     for j in range(2, i):
#         if i%j == 0:
#             break
#     else:
#         lst.append(i)


for i in range(1,10):
    if i in (1,3,5,7):
        break
    print(i)
else:
    print(f"fuck {i}")

