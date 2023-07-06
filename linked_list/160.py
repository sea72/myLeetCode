from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution0:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        stackB = []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        if not stackA or not stackA:
            return None
        ans = None
        while True:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA == nodeB:
                ans = nodeA
            else:
                break
            if not stackA or not stackB:
                break
        return ans

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        while headA:
            setA.add(headA)
            headA = headA.next
        while headB:
            if headB in setA:
                return headB
            headB = headB.next
        return None
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        if currA is None or currB is None:
            return None
        while currA != currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next
        return currA
            



        
            
