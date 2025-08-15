def rank(cards):
    if len(cards) == 2 and 'joker' in cards:
        return 3
    if len(cards) == 4:
        return 2
    else:
        return 1

c = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER'] 
dic = dict(zip(c, range(len(c)))  )
    
def isBigger(a, b):
    if rank(a) != rank(b):
        return a if rank(a) > rank(b) else b
    elif len(a) == len(b):
        return a if dic[a[0]] > dic[b[0]] else b
    else:
        return None

cards = input()
a, b = cards.split('-')
a = a.split()
b = b.split()

res = isBigger(a, b)
if res:
    print(*res)
else:
    print('ERROR')
