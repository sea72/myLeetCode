# Definition for a binary tree node.

from typing import Optional
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        res = 0
        def recurve(curr):
            if not curr:
                return 2
            left = recurve(curr.left)
            right = recurve(curr.right)
            if left == 2 and right == 2:
                return 0
            if left == 0 or right == 0:
                nonlocal res
                res += 1
                return 1
            if left == 1 or right == 1:
                return 2
            return -1 
        
        if recurve(root) == 0:
            res += 1

        return res
    

sol = Solution()
print(sol.minCameraCover(stringToTreeNode('[0,0,null,0,0]')))