from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # change for 5/10/20
        c5, c10 = 0, 0
        for i in bills:
            if i == 5:
                c5 += 1
            if i == 10:
                c5 -= 1
                c10 += 1
                if c5 < 0:
                    return False
            if i == 20:
                c10 -= 1
                c5 -= 1
                if c10 < 0 and c5 >=2 :
                    c5 -= 2
                    c10 += 1
                if c5 < 0 or c10 < 0:
                    return False
        return True

            


sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]))



                


