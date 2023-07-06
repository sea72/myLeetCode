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

from typing import Optional
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        myQ = deque([root])
        while myQ:
            temp = []
            for _ in range(len(myQ)):
                it = myQ.popleft()
                if it:
                    temp.append(it.val)
                    myQ.append(it.left)
                    myQ.append(it.right)
                else:
                    temp.append(None)
            low, high = 0, len(temp)-1
            while low < high:
                if temp[low] != temp[high]:
                    return False
                low += 1
                high -= 1
        return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if (t1 == None and t2 == None):
                return True
            if (t1 == None or t2 == None):
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        return isMirror(root, root)


    

sol = Solution()
root = stringToTreeNode("[5,4,4,1,null,null,1]")
print(sol.isSymmetric(root))

