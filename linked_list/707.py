class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        self.size -= 1
        pred.next = succ
        succ.prev = pred
    

# class MyLinkedList:

#     def __init__(self):
#         self.head = None

#     def get(self, index: int) -> int:
#         node = self.getNode(index)
#         if node is not None:
#             return node.val
#         else:
#             return -1

#     def getNode(self, index: int) -> int:
#         if index < 0:
#             return None
#         pointer = self.head
#         while index > 0:
#             if pointer is None:
#                 return None
#             pointer = pointer.next
#             index -= 1
#         return pointer

#     def addAtHead(self, val: int) -> None:
#         newHead = MyNode(val, self.head)
#         self.head = newHead

#     def addAtTail(self, val: int) -> None:
#         cur = self.head
#         if cur is None:
#             self.addAtHead(val)
#         else:
#             while cur.next:
#                 cur = cur.next
#             cur.next = MyNode(val, None)
                
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index == 0:
#             self.addAtHead(val)
#         else:
#             prev = self.getNode(index-1)
#             if prev is not None:
#                 newNode = MyNode(val, prev.next)
#                 prev.next = newNode

#     def deleteAtIndex(self, index: int) -> None:
#         if index == 0:
#             self.head = self.head.next
#         else:
#             prev = self.getNode(index-1)

#             if prev is not None:
#                 if prev.next is not None:
#                     prev.next = prev.next.next
#                 else:
#                     prev.next = None
        
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.get(1)
obj.deleteAtIndex(0)
obj.get(0)
print('h')

