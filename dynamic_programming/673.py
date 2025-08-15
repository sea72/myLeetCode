from bisect import bisect_left


nums = list(map(int, input().split()))
buckets = []
top = []
buckets.append([])
buckets[0].append((-1, nums[0]))
top.append(nums[0])

def push(k, num):
    if k == 0:
        j = -1
    else:
        j = len(buckets[k-1])-1
    buckets[k].append((j, num))
    top[k] = num

for i in range(1, len(nums)):
    if nums[i] > top[-1]:
        buckets.append([])
        top.append(0)
        push(len(buckets)-1, nums[i])
    else:
        k = bisect_left(top, nums[i])
        push(k, nums[i])

ans = []
i = len(buckets)-1
j = -1
ans = [0] * len(buckets)


while i >= 0:
    if j < 0:
        j1, num = buckets[i][-1]
    else:
        j1, num = buckets[i][j]
    j = j1
    ans[i] = num
    i -= 1
print(ans)


    

