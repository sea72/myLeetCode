from typing import List
class Solution:
    strs = {'2': 'abc', '3':'def', 
                '4' : 'ghi', '5':'jkl', '6':'mno', 
                '7':'pqrs', '8':'tuv', '9':'wxyz'}
    
    def iterCombine(str):
        partA = str[:-1]
        partB = str[-1]
        res = []
        if len(partA) > 1:
            for item in Solution.iterCombine(partA):
                for suffix in Solution.strs[partB]:
                    res.append(item + suffix)
        else:
            for item in Solution.strs[partA]:
                for suffix in Solution.strs[partB]:
                    res.append(item + suffix)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" :
            return []
        elif len(digits) == 1:
            return [ it for it in Solution.strs[digits]]
        else:
            return Solution.iterCombine(digits)

sd = Solution()
a = sd.letterCombinations("23")
print(a)
        