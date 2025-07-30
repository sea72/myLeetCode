from typing import Optional
from MyTreeBase import TreeNode, stringToTreeNode

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur, curParent = root, None
        while cur and cur.val != key:
            curParent = cur
            cur = cur.left if cur.val > key else cur.right
        if cur is None:
            return root
        if cur.left is None and cur.right is None:
            cur = None
        elif cur.right is None:
            cur = cur.left
        elif cur.left is None:
            cur = cur.right
        else:
            successor, successorParent = cur.right, cur
            while successor.left:
                successorParent = successor
                successor = successor.left
            if successorParent.val == cur.val:
                successorParent.right = successor.right
                # 如果 successor 就是 cur.right本身
                # 那么就会涉及到填补的问题
                # 需要将 successor的右子树 提到 successor 当前的位置上来占位，否则这里会是一个None的空位
            else:
                successorParent.left = successor.right
                # successor 只是没有左支，可能有右支
                # 故而需要将 successor的右支接在successorParent的左支上填补空白

            successor.right = cur.right
            successor.left = cur.left
            cur = successor
        if curParent is None:
            return cur
        if curParent.left and curParent.left.val == key:
            curParent.left = cur
        else:
            curParent.right = cur
        return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left or not root.right:
                return root.left if root.left else root.right
            elif root.left and root.right:
                mostL = root.right
                while mostL.left:
                    mostL = mostL.left
                mostL.left = root.left
                return root.right
        return root


sol = Solution()
root = stringToTreeNode("[3,1,5,null,null,4,6]")
sol.deleteNode(root, 5)
