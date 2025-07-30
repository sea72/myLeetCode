from typing import Optional
from MyTreeBase import TreeNode

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur)
            cur = cur.right
        lastVal = 0
        for node in res[::-1]:
            node.val = node.val + lastVal
            lastVal = node.val
        return root