from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(temp, kk):
            if kk == 0:
                nonlocal res
                res.append(temp[:])
            else:
                kk -= 1
                start = temp[-1]+1 if temp else 1
                for num in range(start, n+1):
                    temp.append(num)
                    helper(temp, kk)
                    temp.pop()

        helper([], k)
        return res

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return [list(i) for i in combinations(iterable=range(1, n + 1), r=k)]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        res = []
        def backtrack(curr, n):
            if len(temp) == k:
                res.append(temp[:])
                return
            if curr > n:
                return
            
            # 选择和放弃当前位置都是必须的，看似一样，实则他们当时的temp的长度是不同的
            
            # 选择当前位置
            temp.append(curr)
            backtrack(curr+1, n)
            temp.pop()
            # 跳过当前位置
            backtrack(curr+1, n)
        
        backtrack(1, n)
        return res


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:

#         # 初始化
#         # 将 temp 中 [0, k - 1] 每个位置 i 设置为 i + 1，即 [0, k - 1] 存 [1, k]
#         # 末尾加一位 n + 1 作为哨兵

#         ans = []
#         temp = []
#         for i in range(1, k+1):
#             temp.append(i)
#         # temp.append(n + 1)
        
#         j = 0
#         while (j < k):
#             ans.append(temp[:k])
#             j = 0

#             # 寻找第一个 temp[j] + 1 != temp[j + 1] 的位置 t
#             # 我们需要把 [0, t - 1] 区间内的每个位置重置成 [1, t]

#             while (j < k and temp[j] + 1 == temp[j + 1]):
#                 temp[j] = j + 1
#                 j += 1

#             # j 是第一个 temp[j] + 1 != temp[j + 1] 的位置
#             # 相当于完成了 第j个元素 替换的过程
#             # 是上一个值变成为 下一个值，所以长度也没有发生变化
#             temp[j] += 1
#         return ans


sol = Solution()
print(sol.combine(4, 2))