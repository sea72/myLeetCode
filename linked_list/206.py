from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr is not None:
            temp = ListNode(next = curr.next)
            curr.next = prev
            prev = curr
            curr = temp.next
        return prev

    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None             # 其实只是对原首节点而言不可取代
        return newHead
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next
        newHead = stack.pop()
        cur = newHead
        while len(stack):
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return newHead


