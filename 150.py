from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i.lstrip('-').isnumeric():
                nums.append(int(i))
            else:
                b = nums.pop()
                a = nums.pop()
                if i == "+":
                    a += b
                elif i == "-":
                    a -= b
                elif i == "*":
                    a *= b
                elif i == '/':
                    temp = abs(a)//abs(b) 
                    a = temp if a * b > 0 else -temp
                nums.append(a)
        return nums[-1]

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        nameToFun = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x,y : int(x/y)
        }
        for i in tokens:
            if i.lstrip('-').isnumeric():
                nums.append(int(i))
            else:
                b = nums.pop()
                a = nums.pop()
                nums.append(nameToFun[i](a, b) )
        return nums[-1]