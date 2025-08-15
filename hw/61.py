def sol(m, n):
    if m < 0 or  n < 0:
        return 0
    elif m == 0 or n == 1:
        return 1
    else:
        return sol(m, n-1) + sol(m-n, n)

print(sol(7, 3))
