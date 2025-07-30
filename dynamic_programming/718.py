from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        res = 0

        # 初始化的方式决定了遍历的范围
        # 只初始dp[-1][-1]是不对的，正确的初始化范围要初始dp[-1][1 -> len-1]
        # 所以考虑扩大dp的定义范围，让它在循环中完成正确的初始化
        # 当然不是真的初始化，它的值也是来自于dp[] 默认填0
        # dp = [[0] * n for _ in range(m)]
        # dp[-1][-1] = 1 if nums1[-1] == nums2[-1] else 0
        # for i in range(m-2, -1, -1):
        #     for j in range(n-2, -1, -1):
        #         dp[i][j] = dp[i+1][j+1] + 1 if nums1[i] == nums2[j] else 0
        #         res = max(res, dp[i][j])
        # return res
    

        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if nums1[i] == nums2[j] else 0
                res = max(res, dp[i][j])
        return res


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret
        
        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret
    
sol = Solution()
print(sol.findLength([1,2,3,2,1], [3,2,1,4,7]))