# from dis import dis

# def func(path, no):
#     if no == 5:
#         return
#     else:
#         path.append(no)
#         no += 1
#         func(path, no)

# no = 3
# path = [2]
# func(path, no)
# print(path)

# path = []
# def test():
#     def t1():
#         path.append(2)
#     t1()
#     print(path)
#     path.append(1)
# print(path)

# from collections import Counter
# a = [1,3,2,5,4,3,1]
# ac = Counter(a)
# for i in ac:
#     if i == 2:
#         ac[5] -= 1
#     print(i, ac[i])    

# from random import randint
# start = randint(0, 4)
# def myRange(n=4):

#     cycle = start
#     while not ( cycle // n == 1 and cycle % n == start):
#         yield cycle % n
#         cycle += 1
        
# g = myRange()
# print('t')

# a = [1,2]
# def fun(a):
#     a.append(3)
# fun(a)
# print(a)


# for i in range(5):
#     i += 1
#     print(i)


a = input().split()
print(type(a))