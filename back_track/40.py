from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        temp = []
        canCnt = Counter(candidates)
        def backTrace():
            s = sum(temp)
            if s > target:
                return 
            elif s == target:
                res.add(tuple(sorted(temp)))
                return 
            for item in canCnt:
                if item > target:
                    continue
                if canCnt[item] <= 0:
                    continue
                temp.append(item)
                canCnt[item] -= 1
                backTrace()
                temp.pop()
                canCnt[item] += 1
        
        backTrace()
        return [list(item) for item in res]


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal temp
            if rest == 0:
                ans.append(temp[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return
            
            
            # don't choose present number
            dfs(pos + 1, rest)

            # choose the present number

            # frist item is the number needed
            # the second is the number offered
            most = min(rest // freq[pos][0], freq[pos][1])

            # call element for 1 to most times

            for i in range(1, most + 1):
                temp.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])

            # backTrace 
            temp = temp[:-most]

            
        
        freq = sorted(Counter(candidates).items())
        ans = list()
        temp = list()
        dfs(0, target)
        return ans


class Solution:
    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
            
