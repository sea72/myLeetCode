from typing import Optional
from MyTreeBase import TreeNode

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
        return root
                
        
            