# class Solution:
#     def myAtoi(self, s: str) -> int:
#         value = 0
#         postiveFlag = 1
#         outOfRange = 0
#         mustReadDigitFlag = 0
#         digits = set(["1", "2","3", "4", "5", "6", "7", "8", "9", "0"])
#         digitDic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         def f(s):
#             return digitDic[s]
#         lst = []
#         for it in s:

#             if mustReadDigitFlag and it not in digits:
#                 break
#             if it == " ":
#                 continue
#             elif it == "+":
#                 mustReadDigitFlag = 1
#             elif it == "-":
#                 mustReadDigitFlag = 1
#                 postiveFlag = 0
#             elif it in digits:
#                 mustReadDigitFlag = 1
#                 lst.append(it)
#             else:
#                 break

#         if not lst:
#             return 0
#         for digit in map(f, lst):
#             if abs(value) > 2**31 // 10:
#                 outOfRange = 1
#                 break
#             elif abs(value) == 2**31 // 10:
#                 if postiveFlag and digit >7:
#                     outOfRange = 1
#                     break
#                 elif not postiveFlag and digit >8:
#                     outOfRange = 1
#                     break
#             value = value * 10 + digit

#         if outOfRange:
#             return 2**31-1 if postiveFlag else -2**31
#         if not postiveFlag:
#             value = -value
#         return valueclass Solution:
#     def myAtoi(self, s: str) -> int:
#         value = 0
#         postiveFlag = 1
#         outOfRange = 0
#         mustReadDigitFlag = 0
#         digits = set(["1", "2","3", "4", "5", "6", "7", "8", "9", "0"])
#         digitDic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         def f(s):
#             return digitDic[s]
#         lst = []
#         for it in s:

#             if mustReadDigitFlag and it not in digits:
#                 break
#             if it == " ":
#                 continue
#             elif it == "+":
#                 mustReadDigitFlag = 1
#             elif it == "-":
#                 mustReadDigitFlag = 1
#                 postiveFlag = 0
#             elif it in digits:
#                 mustReadDigitFlag = 1
#                 lst.append(it)
#             else:
#                 break

#         if not lst:
#             return 0
#         for digit in map(f, lst):
#             if abs(value) > 2**31 // 10:
#                 outOfRange = 1
#                 break
#             elif abs(value) == 2**31 // 10:
#                 if postiveFlag and digit >7:
#                     outOfRange = 1
#                     break
#                 elif not postiveFlag and digit >8:
#                     outOfRange = 1
#                     break
#             value = value * 10 + digit

#         if outOfRange:
#             return 2**31-1 if postiveFlag else -2**31
#         if not postiveFlag:
#             value = -value
#         return value

# classical
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         MAX_INT = 2**31 - 1 
#         MIN_INT = -2**31
#         MAX_INT_SUFFIX = MAX_INT%10
#         MAX_INT_PREFIX = MAX_INT//10

#         MIN_INT_SUFFIX = MIN_INT%10 - 10
#         MIN_INT_PREFIX = MIN_INT//10 + 1
#         signedBit = 1
#         s = s.strip()
#         if not s:
#             return 0
#         i, value = 0, 0
#         if s[0] in "+-":
#             i+=1
#             signedBit = 1 if s[0] == "+" else -1
#         while(i<len(s)):
#             if not s[i].isdigit(): break
#             digit = int(s[i]) * signedBit
#             if value > MAX_INT_PREFIX or (value == MAX_INT_PREFIX and digit > MAX_INT_SUFFIX):
#                 value = MAX_INT
#                 break
#             if value < MIN_INT_PREFIX or (value == MIN_INT_PREFIX and digit < MIN_INT_SUFFIX):
#                 value = MIN_INT
#                 break
#             value = value * 10 + digit
#             i += 1
#         return value

# automaton
ABS_INT_MAX = 2**31 -1
ABS_INT_MIN = 2**31
class automaton:
    def __init__(self) -> None:
        self.signed = 1
        self.state = 'start'
        self.value = 0
        self.transform = {'start' : ['start', 'signed', 'readingNum', 'end'],
                          'signed': ['end', 'end', 'readingNum', 'end'], 
                          'readingNum': ['end', 'end', 'readingNum', 'end'],
                          'end': ['end', 'end', 'end', 'end'] }
        
    def moving(self, c : str):
        if c == " ":
            return 0
        elif c in "+-":
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c:str) -> bool:
        self.state = self.transform[self.state][self.moving(c)]
        if self.state == "signed":
            self.signed = 1 if c == "+" else -1
        elif self.state == "readingNum":
            self.value = self.value * 10 + int(c)
            if self.signed > 0 and self.value > ABS_INT_MAX:
                self.value = ABS_INT_MAX
                return True
            elif self.signed < 0 and self.value > ABS_INT_MIN:
                self.value = ABS_INT_MIN
                return True
        elif self.state == "end":
            return True
        else:
            return False
        
    def output(self):
        return self.signed * self.value

class Solution:
    def myAtoi(self, s: str) -> int:
        res = automaton()
        for c in s:
            if res.get(c):
                break
        return res.output()


sol = Solution()
print(sol.myAtoi("-91283472332"))

