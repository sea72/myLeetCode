class Solution0:
    def isHappy(self, n: int) -> bool:
        def next(n):
            res = 0
            while n != 0:
                n, b = divmod(n, 10)
                res += b**2
            return res
        shownSet = set()
        while n not in shownSet:
            if n < 243:
                shownSet.add(n)
            n = next(n)
            if n == 1:
                return True
        return False

class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            res = 0
            while n != 0:
                n, b = divmod(n, 10)
                res += b**2
            return res
        slow = next(n)
        fast = next(slow)
        # while True:
        #     if slow == 1 or fast == 1:
        #         return True
        #     if slow == fast:
        #         return False
        #     slow = next(slow)
        #     fast = next(next(fast))
        while fast != 1 and slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return fast == 1


sol = Solution()
print(sol.isHappy(1))