from MyTreeBase import TreeNode
from typing import Optional

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # if not root:
        #     return None
        # if root.val >= low and root.val <= high:
        #     root.left = self.trimBST(root.left, low, high)
        #     root.right = self.trimBST(root.right, low, high)
        # elif root.val < low:
        #     mostR = root.right
        #     while mostR and mostR.val < low:
        #         mostR = mostR.right
        #     if not mostR:
        #         return None
        #     else:
        #         mostR.left = self.trimBST(mostR.left, low, high)
        #         return mostR
        # elif root.val > high:
        #     mostL = root.left
        #     while mostL and mostL.val > high:
        #         mostL = mostL.left
        #     if not mostL:
        #         return None
        #     else:
        #         mostL.right = self.trimBST(mostL.right, low, high)
        #         return mostL
        # return root

        while root and (root.val < low or root.val > high):
            root = root.right if root.val < low else root.left
        if root is None:
            return None
        node = root
        while node.left:
            if node.left.val < low:
                node.left = node.left.right
            else:
                node = node.left
        node = root
        while node.right:
            if node.right.val > high:
                node.right = node.right.left
            else:
                node = node.right
        return root


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

# 体会递归思路
# 递归是通过return来删除节点的
# 如果一个节点不在区间内，我们通过return它的可能的继承者(可能是None)来删除它
# 如果一个节点在区间内，我们也通过return将问题进一步抛向下一层
