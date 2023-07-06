class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        romanWords = ['M', 'CM', 'D', 'CD',
                      'C', 'XC', 'L', 'XL', 
                      'X', 'IX', 'V', 'IV', 'I']
        order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for k,v in enumerate(order):
            res += num//v * romanWords[k]
            num %= v
        return res

sd = Solution()
print(sd.intToRoman(1995))


