from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonousStack = [0]
        res = [0] * len(temperatures)
        cur = 1
        while cur < len(temperatures):
            if temperatures[cur] <= temperatures[monotonousStack[-1]]:
                monotonousStack.append(cur)
            else:
                while monotonousStack and temperatures[monotonousStack[-1]] < temperatures[cur]:
                    temp = monotonousStack.pop()
                    res[temp] = cur - temp
                monotonousStack.append(cur)
            cur += 1
        return res
    

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            # 调换位置，把pop放在前面，注意while要先检测栈非空
            while stack and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
