from typing import Optional

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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def isExist(k, level) -> bool:
            bits = 1 << (level-1)
            cur = root
            while bits > 0:
                if (bits & k) == 0:
                    cur = cur.left
                else:
                    cur = cur.right
                if cur is None:
                    return False
                bits >>= 1
            return True
        
        cur = root
        depth = -1
        while cur:
            cur = cur.left
            depth += 1
        low, high = 2 ** depth, 2 ** (depth+1) -1
        while low < high:
            mid = (low + high + 1) // 2
            if isExist(mid, depth):
                low = mid
            else:
                high = mid - 1
        return low
    

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            if leftDepth > rightDepth:
                # return self.countNodes(root.left) + 1 + 2 ** rightDepth - 1
                return self.countNodes(root.left) + (1 << rightDepth)
            else:
                return self.countNodes(root.right) + (1 << leftDepth)

    def maxDepth(self, node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth

    
sol = Solution()
root = stringToTreeNode("[5,4,6]")
print(sol.countNodes(root))
