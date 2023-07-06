# Definition for a binary tree node.
from typing import Optional
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = Node(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = Node(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = Node(rightNumber)
            nodeQueue.append(node.right)
    return root

# 初始状态下，所有 next 指针都被设置为 None
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        myQue = deque([root])
        while myQue:
            myQueLen = len(myQue)
            for no in range(myQueLen):
                front = myQue.popleft()
                back = myQue[0] if no < myQueLen - 1 else None
                front.next = back
                if front.left:
                    myQue.append(front.left)
                if front.right:
                    myQue.append(front.right)
        return root
    
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        cur = root
        # 节点next默认置None,故只修改非None的即可
        while cur.left:
            parentLevelHead = cur
            while parentLevelHead:
                parentLevelHead.left.next = parentLevelHead.right
                if parentLevelHead.next:
                    parentLevelHead.right.next = parentLevelHead.next.left
                parentLevelHead = parentLevelHead.next
            cur = cur.left
        return root
    
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        elif root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root



sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.connect(root))