from typing import Optional,List
from collections import deque
from MyTreeBase import stringToTreeNode, TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        if cur:
            cur.left, cur.right = cur.right, cur.left
            self.invertTree(cur.left)
            self.invertTree(cur.right)
        return cur

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        stack = []
        while cur or stack:
            while cur:
                cur.left, cur.right = cur.right, cur.left
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack.append(cur.right)
                stack.append(cur.left)
        return root
    
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
root = sol.invertTree(root)
print(sol.levelOrder(root))


            


