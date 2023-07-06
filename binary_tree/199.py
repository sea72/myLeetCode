# Definition for a binary tree node.
from typing import Optional, List
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

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        myQue = deque([root])
        res = []
        while myQue:
            temp = []
            for _ in range(len(myQue)):
                item = myQue.popleft()
                temp.append(item.val)
                if item.left:
                    myQue.append(item.left)
                if item.right:
                    myQue.append(item.right)
            res.append(temp[-1])
        return res

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = dict()
        depth = 1
        stack = [(root, 0)]
        while stack:
            for _ in range(len(stack)):
                item = stack.pop()
                
                res.setdefault(depth, item.val)

                if item.left:
                    stack.append((item.left, depth + 1))
                if item.right:
                    stack.append((item.right, depth + 1))
            depth += 1
        return res
    
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root , 1)]
        while stack:
            item = stack.pop()
            depth = item[1]
            if len(res) < item[1]:
                res.append(item[0].val)
            if item[0].left:
                stack.append((item[0].left, depth+1))
            if item[0].right:
                stack.append((item[0].right, depth+1))
        return res
            


sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.rightSideView(root))



        