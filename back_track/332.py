from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        temp = ['JFK']
        used = [0] * len(tickets)
        tickets.sort()

        def dfs(remain):
            if remain == 0:
                res.append(temp[:])
                return True
            for n in range(len(tickets)):
                if used[n] == 0 and tickets[n][0] == temp[-1]:
                    used[n] = 1
                    temp.append(tickets[n][1])
                    flag = dfs(remain-1)
                    used[n] = 0
                    temp.pop()
                    if flag:
                        return True
        
        dfs(len(tickets))
        return res[0]

# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         tickets.sort() # 先排序，这样一旦找到第一个可行路径，一定是字母排序最小的
#         used = [0] * len(tickets)
#         path = ['JFK']
#         results = []
#         self.backtracking(tickets, used, path, 'JFK', results)
#         return results[0]
    
#     def backtracking(self, tickets, used, path, cur, results):
#         if len(path) == len(tickets) + 1:  # 终止条件：路径长度等于机票数量+1
#             results.append(path[:])  # 将当前路径添加到结果列表
#             return True
        
#         for i, ticket in enumerate(tickets):  # 遍历机票列表
#             if ticket[0] == cur and used[i] == 0:  # 找到起始机场为cur且未使用过的机票
#                 used[i] = 1  # 标记该机票为已使用
#                 path.append(ticket[1])  # 将到达机场添加到路径中
#                 state = self.backtracking(tickets, used, path, ticket[1], results)  # 递归搜索
#                 path.pop()  # 回溯，移除最后添加的到达机场
#                 used[i] = 0  # 标记该机票为未使用
#                 if state:
#                     return True  # 只要找到一个可行路径就返回，不继续搜索

import heapq
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = list()
        dfs("JFK")
        return stack[::-1]


sol = Solution()
inp = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] 
print(len(inp))
print(sol.findItinerary(inp))
