from typing import Optional
from MyTreeBase import TreeNode, stringToTreeNode
from collections import deque
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.sort()
        value = float('inf')
        for i in range(len(res)-1):
            if abs(res[i] - res[i+1]) < value:
                value = abs(res[i] - res[i+1])
        return value

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        curr = root
        mostR = None
        pre = -1
        res = float('inf')
        while curr:
            if curr.left:
                mostR = curr.left
                while mostR.right and mostR.right != curr:
                    mostR = mostR.right
                if mostR.right == curr:
                    if pre != -1 and abs(curr.val - pre) < res:
                        res = abs(curr.val - pre)
                    pre = curr.val
                    mostR.right = None
                    curr = curr.right
                else:
                    mostR.right = curr
                    curr = curr.left
            else:
                if pre != -1 and abs(curr.val - pre) < res:
                    res = abs(curr.val - pre)
                pre = curr.val
                curr = curr.right
        return res
    
sol = Solution()
print(sol.getMinimumDifference(stringToTreeNode("[1,null,3,2]")))
