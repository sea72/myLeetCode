def kmp(query, pattern):
    n, m = len(query), len(pattern)
    fail = [-1] * m
    for i in range(1, m):
        j = fail[i - 1]
        while j != -1 and pattern[j + 1] != pattern[i]:
            j = fail[j]
        if pattern[j + 1] == pattern[i]:
            fail[i] = j + 1
    match = -1
    for i in range(n):
        while match != -1 and pattern[match + 1] != query[i]:
            match = fail[match]
        if pattern[match + 1] == query[i]:
            match += 1
            if match == m - 1:
                return True
    return False


res = kmp('abcdabcfabc', 'abcfabc')
print(res)