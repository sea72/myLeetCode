from MyTreeBase import TreeNode, stringToTreeNode
from typing import Optional
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isTrue(node, min, max):
            if not node:
                return True
            return node.val > min and node.val < max and isTrue(node.left, min, node.val) and isTrue(node.right, node.val, max)
        return isTrue(root, -math.inf, math.inf)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = -math.inf
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= curr:
                return False
            else:
                curr = root.val
            root = root.right
        return True


root = stringToTreeNode("[2,2,2]")
sol = Solution()
print(sol.isValidBST(root))

