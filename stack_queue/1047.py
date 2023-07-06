class Solution0:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append()
        return ''.join(stack)
    
class Solution1:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s
        sList = list(s)
        slow, fast = 0, 1 
        while fast < len(sList):
            if sList[fast] == sList[slow]:
                sList[slow:fast+1] = []
                if slow > 0:
                    slow -= 1
                    fast -= 1
            else:
                fast += 1
                slow += 1
        return ''.join(sList)
    
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        while fast < len(res):
            res[slow] = res[fast]
            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[:slow])

sol = Solution()
print(sol.removeDuplicates('abbacddc'))

            
            
            

