from typing  import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        dp = [[0] * n for _ in range(n)]
        res = 0

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = heights[i]
                else:
                    dp[i][j] = min(dp[i][j-1] // (j-i), heights[j]) * (j-i+1)
                res = max(res, dp[i][j])

        return res

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            minHeight = heights[i]
            for j in range(i, n):
                minHeight = min(minHeight, heights[j])
                res = max(res, minHeight * (j-i+1))

        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

sol = Solution()
print(sol.largestRectangleArea( [2,1,5,6,2,3]))