s = input()
n = int(input())
m = s.count('G') + s.count('C')
end = n
maxEnd = 0
maxGC = 0
while end <= len(s):
    m = s[end-n:end].count('G') + s[end-n:end].count('C')
    if m > maxGC:
        maxGC = m
        maxEnd = end
    end += 1
print(s[maxEnd-n:maxEnd])