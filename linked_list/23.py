# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (len(lists) == 1 and not lists[0]):
            return None
        
        def mergetTwoLists(fronter, latter):
            if not fronter or not latter:
                return fronter if fronter else latter
            dummyHead = ListNode()
            cur = dummyHead
            while fronter and latter:
                if fronter.val < latter.val:
                    cur.next = fronter
                    fronter = fronter.next
                else:
                    cur.next = latter
                    latter = latter.next
                cur = cur.next
            cur.next = fronter if fronter else latter
            return dummyHead.next
        
        res = ListNode()
        for no in range(len(lists)):
            res = mergetTwoLists(res, lists[no])
        return res
    
b = ListNode(2, None)
a = ListNode(1, b)
d = ListNode(4, None)
c = ListNode(3, d)
lists = [a, c]
sol = Solution()
res = sol.mergeKLists(lists)
while res:
    print(res.val)
    res = res.next