from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        temp = []
        real = []
        usedX = [0] * n

        def inSlash(x, y):
            for queen in temp:
                ratio = ( y - queen[1] ) / ( x - queen[0] )
                if abs(ratio) == 1:
                    return True
            return False

        def dfs(level):
            if level == n:
                res.append(temp[:])
                return
            for i in range(n):
                if usedX[i] == 0 and not inSlash(i, level):
                    temp.append((i, level))
                    usedX[i] = 1
                    dfs(level+1)
                    temp.pop()
                    usedX[i] = 0
        
        def style():
            for item in res:
                ans = []
                for queen in item:
                    base = ""
                    for t in range(n):
                        if t == queen[0]:
                            base += "Q"
                        else:
                            base += "."
                    ans.append(base)
                real.append(ans)

        
        dfs(0)
        style()
        return real

sol = Solution()
print(sol.solveNQueens(4))




