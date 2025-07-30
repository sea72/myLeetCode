from functools import cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)
    

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b = 0, 1
        for _ in range(n-1):
            c = a + b
            a, b = b, c
        return c
    
sol = Solution()
print(sol.fib(6))