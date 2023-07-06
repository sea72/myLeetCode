# Definition for a binary tree node.
from typing import Optional
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


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = root
        while first:  # 遍历每一层
            dummyHead = Node(None)  # 为下一行创建一个虚拟头节点，相当于下一行所有节点链表的头结点(每一层都会创建)；
            tail = dummyHead  # 为下一行维护一个尾节点指针（初始化是虚拟节点）
            cur = first
            while cur:  # 遍历当前层的节点
                if cur.left:  # 链接下一行的节点
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next  # cur同层移动到下一节点
            first = dummyHead.next  # 此处为换行操作，更新到下一行
        return root
    

sol = Solution()
root = stringToTreeNode("[3,9,20,null,null,15,7]")
print(sol.connect(root))