from typing import Optional
from MyTreeBase import TreeNode, stringToTreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            
            # left child tree
            leftHeight = height(root.left)

            # right child tree
            rightHeight = height(root.right)

            # parent node 
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            
            # left child tree
            leftHeight = height(root.left)

            if leftHeight == -1:
                return -1

            # right child tree
            rightHeight = height(root.right)

            # parent node 
            if rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0

    
root = stringToTreeNode("[1,null,2,null,3]")
sol = Solution()
print(sol.isBalanced(root))
