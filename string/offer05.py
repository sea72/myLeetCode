class Solution0:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

class Solution1:
    def replaceSpace(self, s: str) -> str:
        sList = list(s)
        for item in range(len(sList)):
            if sList[item] == " ":
                sList[item] = '%20'
        return ''.join(sList)
    
class Solution2:
    def replaceSpace(self, s: str) -> str:
        ans = ''
        for i in s:
            if i == ' ':
                ans += '%20'
            else:
                ans += i
        return ans
    

a = [1,2,3]
for i in a:
    i = 3
print(a)