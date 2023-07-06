from typing import List 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maxVol = 0
        while( i!= j ):
            s = (j-i) * min(height[i], height[j])
            maxVol = max(s, maxVol)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxVol
    
sd =  Solution()
print(sd.maxArea([1,8,6,2,5,4,8,3,7]))


