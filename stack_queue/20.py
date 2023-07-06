class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        opposite = {'[':']', '(':')', '{':'}'}
        for i in s:
            if i in opposite.keys():
                myStack.append(i)
                continue
            if i in opposite.values() and myStack and opposite[myStack[-1]] == i:
                myStack.pop()
            else:
                return False
        
        # 不能消掉的右括号就直接添加到stack里，反正最后一定会返false
        # for ch in s:
        #     if ch in pairs:
        #         if not stack or stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(ch)
    

        return not myStack

sol = Solution()
print(sol.isValid("]"))


                
            

            

