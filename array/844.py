class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sPtr, tPtr = len(s)-1, len(t) -1
        sSkip, tSkip = 0, 0
        while sPtr >= 0 or tPtr >= 0:
            while sPtr >= 0:
                if s[sPtr] == '#':
                    sSkip += 1
                    sPtr -= 1
                elif sSkip:
                    sPtr -= 1
                    sSkip -= 1
                else:
                    break
            while tPtr >= 0:
                if t[tPtr] == '#':
                    tSkip += 1
                    tPtr -= 1
                elif tSkip:
                    tPtr -= 1
                    tSkip -= 1
                else:
                    break
            if sPtr >= 0 and tPtr >= 0:
                if s[sPtr] != t[tPtr]:
                    return False
            elif sPtr >= 0 or tPtr >= 0:
                return False
            sPtr -= 1
            tPtr -= 1
        return True

s = "nzp#o#g"
t = "b#nzp#o#g"
sd = Solution().backspaceCompare(s,t)
print(sd)



