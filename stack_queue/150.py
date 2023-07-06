from typing import List
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(n1, n2, sig):
            if sig == '+':
                return n1 + n2
            elif sig == '-':
                return n1 - n2
            elif sig == '*':
                return n1 * n2
            elif sig == '/':
                # if n1 % n2 == 0:
                #     return n1 // n2
                # else:
                #     return n1//n2 if n1//n2 >= 0 else n1//n2 + 1
                return math.trunc(n1/n2)

        stack = []
        signals = ['+', '-', '*', '/']
        for it in tokens:
            if it in signals:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(cal(n1, n2, it))
            else:
                stack.append(int(it))
        return stack[-1]
    
sol = Solution()
print(sol.evalRPN(["4","-2","/","2","-3","-","-"]))