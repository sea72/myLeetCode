from typing import List
class Solution1:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        basket = set()
        res = 2
        low, high = 1, 2
        i = 0
        while i < len(fruits) - 1:
            basket = set([fruits[i], fruits[i+1]])
            quantity = 2
            high = i + 2
            while high < len(fruits) and fruits[high] in basket:
                quantity += 1
                high += 1
            low = i - 1
            while low >= 0 and fruits[low] in basket:
                quantity += 1
                low -= 1
            res = max(res, quantity)
            i = high - 1
        return res

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        from collections import Counter
        cnt = Counter()
        left = 0 
        quantity = 1
        for right in range(len(fruits)):
            cnt[fruits[right]] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            quantity = max(right - left + 1, quantity)
        return quantity


            






fruits = [0,1,1]
print(Solution().totalFruit(fruits))
            
