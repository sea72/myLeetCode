from MyTreeBase import TreeNode, stringToTreeNode
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def dfs(node, p, q):
#             if not node:
#                 return False
#             lson = dfs(node.left, p, q)
#             rson = dfs(node.right, p, q)
#             if (lson and rson) or ((node.val == p.val or node.val == q.val) and (lson or rson)):
#                 nonlocal ans
#                 ans = node
#             return lson or rson or (node.val == p.val or node.val == q.val)
        
#         ans = None
#         dfs(root, p, q)
#         return ans

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
    

sol = Solution()
node = stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
print(sol.lowestCommonAncestor(node, TreeNode(5), TreeNode(1)).val)