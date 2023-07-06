from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = Counter()
        for _ in s:
            cnt[_] += 1
        for _ in t:
            cnt[_] -= 1
            if cnt[_] == 0:
                cnt.pop(_)
        if len(cnt) == 0:
            return True
        else:
            return False

s = "rat"
t = "car"
sol = Solution()
print(sol.isAnagram(s,t))