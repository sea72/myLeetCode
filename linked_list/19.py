# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        pre, slow, fast = dummy, head, head
        for _ in range(n):
            fast = fast.next
        while fast:
            pre = pre.next
            slow = slow.next
            fast = fast.next
        pre.next = slow.next
        return dummy.next


d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

sd = Solution()
res = sd.removeNthFromEnd(a, 2)
print(res)

        