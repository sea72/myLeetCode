from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]
        res = 0

        for i in range(1, n):
            leftMax[i] = max( leftMax[i-1], height[i] )
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i] 
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()
                if stack:
                    left = stack[-1]
                    res += (min(height[left], h) - height[bottom]) * (i - left - 1)
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []

        for h in height:
            while stack and stack[-1] < h:
                stack.pop()
            stack.append(h)
            print(stack)
        return stack


sol = Solution()
print(sol.trap([1,2,3,4,5,2,5,6,7,3,7,3,65,8,9,4,5,6,7]))

        




            

            
        
            