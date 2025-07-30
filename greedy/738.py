class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = []
        while True:
            digits.insert(0, n%10)
            n = n//10
            if n == 0:
                break
        
        def check(digits):
            key = digits[0]
            for no in range(1, len(digits)):
                if digits[no] < key:
                    return False, no
                else:
                    key = digits[no]
            return True, 0
        
        def ans(digits):
            res = 0
            for d in digits:
                res = res * 10 + d
            return res
                    
        while True:
            flag, no = check(digits=digits)
            if flag:
                break
            else:
                n = no - 1
                while digits[n] == 0 and n > 0:
                    digits[n] = 9
                    n -= 1
                digits[n] -= 1
                for n in range(no, len(digits)):
                    digits[n] = 9

        return ans(digits)

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n = list(str(n))
        for i in range(len(str_n)):
            if i == len(str_n)-1:
                break
            if str_n[i] > str_n[i+1]:
                break
        if i < len(str_n)-1:
            while i >= 0 and str_n[i] > str_n[i+1]:
                int_i = int(str_n[i])
                int_i -= 1
                str_n[i] = str(int_i)
                i -= 1
            i += 2
            while i <= len(str_n) - 1:
                str_n[i] = '9'
                i += 1
        return int(''.join(str_n))
# str object is not mutable 


sol = Solution()
print(sol.monotoneIncreasingDigits(n = 9527))
