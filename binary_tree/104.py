# Definition for a binary tree node.
from typing import Optional
import math
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurveDepth(cur):
            if not cur:
                return 0
            else:
                return max(recurveDepth(cur.left), recurveDepth(cur.right)) + 1
        return recurveDepth(root)
    

    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recurveDepth(cur):
            if cur is None:
                return math.inf
            if cur.left is None and cur.right is None:
                return 1
            else:
                return min(recurveDepth(cur.left), recurveDepth(cur.right)) + 1
        return recurveDepth(root)
    

            
sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.maxDepth(root))
