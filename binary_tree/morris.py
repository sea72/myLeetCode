from typing import Optional, List
import functools
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
    def name(func):
        @functools.wraps(func)
        def newFunc(*args, **argv):
            print(func.__name__)
            return func(*args, **argv)
        return newFunc


    @name
    def morris(self, root: TreeNode) -> List[int]:
        cur = root
        mostR = None
        res = []
        while cur:
            res.append(cur.val)
            if cur.left:
                mostR = cur.left
                while mostR.right and mostR.right != cur:
                    mostR = mostR.right
                if mostR.right == cur:
                    mostR.right = None
                    cur = cur.right
                else:
                    mostR.right = cur
                    cur = cur.left
            else:
                cur = cur.right
        return res
    
    @name
    def morrisPre(self, root: TreeNode) -> List[int]:
        cur = root
        mostR = None
        res = []
        while cur:
            if cur.left:
                mostR = cur.left
                while mostR.right and mostR.right != cur:
                    mostR = mostR.right
                if mostR.right == None:
                    mostR.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    mostR.right = None
                    cur = cur.right
            else:
                res.append(cur.val)
                cur = cur.right
        return res

    @name
    def morrisPost(self, root: TreeNode) -> List[int]:
        cur = root
        mostR = None
        res = []
        while cur:
            if cur.left:
                mostR = cur.left
                while mostR.right and mostR.right != cur:
                    mostR = mostR.right
                if mostR.right == None:
                    mostR.right = cur
                    cur = cur.left
                else:
                    mostR.right = None
                    res += self.printEdge(cur.left)
                    cur = cur.right
            else:
                cur = cur.right
        res += self.printEdge(root)
        return res

    def printEdge(self, start):
        if not start.right:
            return [start.val]
        else:
            res = []
            tail = self.reverseEdge(start)
            cur = tail
            while cur:
                res.append(cur.val)
                cur = cur.right
            self.reverseEdge(tail)
            return res

    def reverseEdge(self, start):
        pre, cur = None, start
        while cur:
            next = cur.right
            cur.right = pre
            pre = cur
            cur = next
        return pre

    @name
    def morrisIn(self, root: TreeNode) -> List[int]:
        cur = root
        res = []
        mostR = None
        while cur:
            if cur.left:
                mostR = cur.left
                while mostR.right and mostR.right != cur:
                    mostR = mostR.right
                if mostR.right == None:
                    mostR.right = cur
                    cur = cur.left
                else:
                    mostR.right = None
                    res.append(cur.val)
                    cur = cur.right
            else:
                res.append(cur.val)
                cur = cur.right
        return res



        
                
                

sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.morris(root))
print('-'*20)
print(sol.morrisPost(root))
print('-'*20)
print(sol.morrisPre(root))
print('-'*20)
print(sol.morrisIn(root))
