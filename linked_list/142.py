class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

from typing import Optional
class Solution0:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSet = set()
        while head:
            if head in nodeSet:
                return head
            nodeSet.add(head)
            head = head.next
        return None
    
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        cycleLen = 0
        stop = False
        while True:
            if slow is None or fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                if stop:
                    break
                else:
                    stop = True
                    cycleLen = 1
            else:
                cycleLen += 1
        
        # 因为slow和fast不一定是从环里开始进行追及问题的，所以计算环的长度用这个方法有错
        # 所以必须等slow == fast确认二者都进环了再从新开始追及

        curr = head
        while True:
            temp = curr
            for _ in range(cycleLen):
                temp = temp.next
            if temp == curr:
                return curr
            else:
                curr = curr.next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow, fast = head, head
        while fast:
            # 省略掉了slow的非空检验，为什么？
            # 因为fast已经扫过了，确认了安全
            slow = slow.next   
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                ptrNode = head
                while ptrNode != slow:
                    ptrNode = ptrNode.next
                    slow = slow.next
                return ptrNode
        return None

        
node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
node4.next = node2
so = Solution()
res = so.detectCycle(node1)
print(res.val)   
            
            
        
