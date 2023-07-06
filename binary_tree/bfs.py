# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
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
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution0:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        firstQue = deque([root])
        secondQue = deque()
        curr = None
        res = []
        while firstQue or secondQue:
            temp = []
            while firstQue:
                curr = firstQue.popleft()
                temp.append(curr.val)
                if curr.left:
                    secondQue.append(curr.left)
                if curr.right:
                    secondQue.append(curr.right)
            res.append(temp)
            if secondQue:
                firstQue = secondQue.copy()
                secondQue.clear()
        return res
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            myQue = deque([root])
        res = []
        while myQue:
            level = []
            for _ in range(len(myQue)):
                item = myQue.popleft()
                level.append(item.val)
                if item.left:
                    myQue.append(item.left)
                if item.right:
                    myQue.append(item.right)
            res.append(level)
        return res
    
sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.levelOrder(root))


