from typing import List
from collections import Counter
class Solution0:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        hashtable = Counter()
        for a in range(len(nums1)):
            for b in range(len(nums2)):
                hashtable[nums1[a] + nums2[b]] += 1
        # for a in range(len(nums3)):
        #     for b in range(len(nums4)):
        #         hashtable2[nums3[a] + nums4[b]] += 1
        # for k in hashtable:
        #     if -k in hashtable2:
        #         res += hashtable[k] * hashtable2[-k]
        # return res
        for c in range(len(nums3)):
            for d in range(len(nums4)):
                temp = nums3[c] + nums4[d]
                res += hashtable[-temp]
        return res

import collections
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ds1 = collections.Counter(nums1)
        ds2 = collections.Counter(nums2)
        ds3 = collections.Counter(nums3)
        ds4 = collections.Counter(nums4)
        # nums1 and nums2
        add12 = collections.defaultdict(int)
        add34 = collections.defaultdict(int)
        for k1, v1 in ds1.items():
            for k2, v2 in ds2.items():
                add12[k1 + k2] += (v1 * v2)
        for k1, v1 in ds3.items():
            for k2, v2 in ds4.items():
                add34[k1 + k2] += (v1 * v2)
        count = 0
        for k1, v1 in add12.items():
            if -k1 in add34:
                count += (v1 * add34[-k1])
        return count
    
sol = Solution()
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(sol.fourSumCount(nums1, nums2, nums3, nums4))

