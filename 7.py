class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        while x!=0:
            if new > 214748364 or new < -214748364:
                return 0
            else:
                if x>0:
                    digit = x%10
                    x //= 10
                else:
                    digit = x%10 - 10
                    digit = 0 if digit == -10 else digit
                    x = (x - digit)// 10
                new = new * 10 + digit
        return new

            
ans = Solution()
print(ans.reverse(x = -100))