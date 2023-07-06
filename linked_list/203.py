# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(head)
        prev, cur = dummyNode, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummyNode.next
    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


no7 = ListNode(6, None)
no6 = ListNode(5, no7)
no5 = ListNode(4, no6)
no4 = ListNode(3, no5)
no3 = ListNode(6, no4)
no2 = ListNode(2, no3)
no1 = ListNode(1, no2)
sol = Solution()
res = sol.removeElements(no1, 6)
print('h')


