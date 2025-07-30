from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)
        
        return ret
    
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        caddys = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                caddys[i] = caddys[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                caddys[i] = max(caddys[i+1]+1, caddys[i])
        
        return sum(caddys)

sol = Solution()
print(sol.candy([8,9,8,9,10,9,8,9,8,7,7,6,5,6]))
