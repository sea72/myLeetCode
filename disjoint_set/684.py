from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        fathers = [0] * (n+1)
        for i in range(n+1):
            fathers[i] = i

        # def find(x):
        #     if fathers[x] == x:
        #         return x
        #     else:
        #         return find(fathers[x])

        # store the value
        def find(x):
            if fathers[x] != x:
                fathers[x] = find(fathers[x])
            return fathers[x]
        
        for edge in edges:
            s, e = edge
            rootS, rootE = find(s), find(e)
            if rootS == rootE:
                return edge
            else:
                fathers[rootE] = rootS

sol = Solution()
print(sol.findRedundantConnection(edges = [[2,1],[3,1],[4,2],[1,4]]))
