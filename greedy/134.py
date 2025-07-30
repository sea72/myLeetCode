from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        profit = [ gas[no] - cost[no] for no in range(n) ]
        start = 0
        while start < n:
            cnt = 0
            remain = 0
            while cnt < n:
                cur = (start + cnt) % n
                remain += profit[cur]
                if remain < 0:
                    break
                cnt += 1
            if cnt == n:
                return start
            else:
                # Key Point
                # Q: Why we don't use   start = cur + 1
                # A: Because the cur is remainder, it's in a cycle.
                #    Use cur may make start into a cycle. 
                start = start + cnt + 1
        return -1


sol = Solution()
gas = [2,3,4]
cost = [3,4,3]
print(sol.canCompleteCircuit(gas, cost))

