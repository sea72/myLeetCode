from typing import List

class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))
    
    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)
    
    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        parent = list(range(n + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                # situation A & B | 入度为2
                # one edge can't be mark as conflict and cycle at the same time due to the if statement
                conflict = i
            else:
                # situation C | 入度为1
                # 正常记录
                parent[node2] = node1
                # 检查是否成环
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    # 无环则正常加入并查集
                    uf.union(node1, node2)
        
        # situation C
        # remove the last edge making cycle
        if conflict < 0:
            # return [edges[cycle][0], edges[cycle][1]]
            return edges[cycle]
        else:
            # situation A & B
            conflictEdge = edges[conflict]
            # if both cycle and conflict
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]


sol = Solution()
print(sol.findRedundantDirectedConnection([ [4,2], [2,3], [3,1], [1,2] ]))