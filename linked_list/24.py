# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = self.swapPairs(head.next.next)
        head.next.next = head
        ans = ListNode(next = head.next)
        head.next = newHead
        return ans.next
    
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        temp = dummyHead
        while temp.next and temp.next.next:
            nodeOne = temp.next
            nodeTwo = temp.next.next
            nodeOne.next = nodeTwo.next
            nodeTwo.next = nodeOne
            temp.next = nodeTwo
            temp = nodeOne
        return dummyHead.next



            