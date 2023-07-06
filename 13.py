class Solution:
    def romanToInt(self, s: str) -> int:
        romanWords = ['M', 'CM', 'D', 'CD',
                'C', 'XC', 'L', 'XL', 
                'X', 'IX', 'V', 'IV', 'I']
        order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanDic = dict(zip(romanWords, order))
        num = 0
        i = 0
        while i<len(s):
            if s[i:i+2] in romanDic:
                num += romanDic[s[i:i+2]]
                i+=2
            else:
                num += romanDic[s[i]]
                i+=1
        return num

sd = Solution()
print(sd.romanToInt("MCMXCIV"))