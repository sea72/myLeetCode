class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        # G[0] 必须设置为1,否则就无法得到正确结果
        G[0], G[1] = 1, 1
        for length in range(2, n+1):
            for i in range(1, length+1):
                G[length] += G[length-i] * G[i-1]
        return G[n]
    
sol = Solution()
print(sol.numTrees(3))