def getNext(T):
    next = [-1] * len(T)
    # i表示当前当前需要比对的主串的位置
    i = 0
    # j = -1是设置问题,或者说我们手动模拟了T串T[0]的next求值过程，T[0]不匹配要那么T要跳转到T[-1]，也即下一次T串提供参与比较的是T[0]
    # 通过这种设置间接达成了某位置的PMT是前一位的最大真公共前后缀
    j = -1
    while i < len(T)-1:
        if j == -1 or T[i] == T[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

def getNext2(T):
    m = len(T)
    fail = [-1] * m
    for i in range(1, m):
        j = fail[i - 1]
        while j != -1 and T[j + 1] != T[i]:
            j = fail[j]
        if T[j + 1] == T[i]:
            fail[i] = j + 1
    return fail

    # for i in range(1, n - 1):
    #     while match != -1 and pattern[match + 1] != query[i]:
    #         match = fail[match]
    #     if pattern[match + 1] == query[i]:
    #         match += 1
    #         if match == m - 1:
    #             return True
    # return False


def getPMT(T):
    pmt = [0]
    j = 0
    for i in range(1, len(T)):
        while j > 0 and T[j] != T[i]:
            j = pmt[j-1]
        if T[j] == T[i]:
            j += 1
        pmt.append(j)
    return pmt

def KMP(S, T):
    i = 0
    j = 0
    next = getNext(T)
    while i < len(S) and j < len(T):
        #j == -1 找无可找，从 S[i+1] 开始和 T[0] 匹配 or 当匹配成功时，往下匹配。
        if j == -1 or S[i] == T[j]:
            i += 1
            j += 1
        # 匹配不成功则用 next(j) 找下一次匹配的位置
        else:
            j = next[j]
    # 如果模式串在主串中存在
    if j == len(T):
        return i - j
    else:
        return -1
    

T = 'aabaaf'
print(getNext(T))
print(getNext2(T))
print(getPMT(T))