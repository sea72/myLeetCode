import random
i = 0

def test():
    a = [ random.randint(-100, 100) for _ in range(5)]
    a.sort()
    low , high = 0, len(a)-1
    target = a[random.randint(0, 4)]
    while low < high:
        mid = (low + high) // 2 + 1
        if a[mid] < target:
            low = mid + 1
        else:
            high = mid
    if low == high and low - mid == 1:
        global i
        i += 1
    else:
        print('h')

if __name__ == "__main__":
    for time in range(1000):
        test()
    print(i)



