from  MyTreeBase import TreeNode, stringToTreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return root
    
root = stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
sol = Solution()
print(sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val)
