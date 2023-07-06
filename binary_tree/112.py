from typing import Optional
from MyTreeBase import TreeNode, stringToTreeNode
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        res = False
        def findPathSum(cur, sum):
            nonlocal res
            if not cur or res:
                return
            else:
                sum += cur.val
                if not cur.left and not cur.right:  
                    res |= (sum == targetSum)
                else:
                    findPathSum(cur.left, sum)
                    findPathSum(cur.right, sum)

        findPathSum(root, 0)
        return res

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.hasPathSum(root, 10))

                
            
