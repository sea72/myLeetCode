from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set()
        for _ in nums1:
            numSet.add(_)
        ans = set(_ for _ in nums2 if _ in numSet)
        return list(ans)
