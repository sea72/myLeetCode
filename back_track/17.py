from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictDigit = ["2", "3", "4", "5", "6", "7", "8", "9"]
        dictAlpha = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        dic = dict(zip(dictDigit, dictAlpha))

        res = []
        temp = []
        def read(cur):
            if cur == len(digits):
                res.append("".join(temp))
                return
            num = digits[cur]
            alphas = dic[num]
            for alpha in alphas:
                temp.append(alpha)
                read(cur + 1)
                temp.pop()
        # special occasions
        if len(digits) == 0:
            return res
        digits = list(digits)
        read(0)
        return res
    
sol = Solution()
print(sol.letterCombinations("96"))
