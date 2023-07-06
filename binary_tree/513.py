from typing import Optional
from MyTreeBase import TreeNode, stringToTreeNode
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        myQ = deque([root])
        # while myQ:
        #     temp = []
        #     for _ in range(len(myQ)):
        #         cur = myQ.popleft()
        #         temp.append(cur.val)
        #         if cur.left:
        #             myQ.append(cur.left)
        #         if cur.right:
        #             myQ.append(cur.right)
        # return temp[0]
        while myQ:
            cur = myQ.popleft()
            if cur.right:
                myQ.append(cur.right)
            if cur.left:
                myQ.append(cur.left)
            res = cur.val
        return res
            


