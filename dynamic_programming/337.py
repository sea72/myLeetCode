from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        f, g = {} , {}
        f[None], g[None] = 0, 0
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val + g[node.left] + g[node.right]
            g[node] = max(f[node.left], g[node.left]) + max(f[node.right], g[node.right])

        dfs(root)
        return max(f[root], g[root])

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0
            leftF, leftG = dfs(node.left)
            rightF, rightG = dfs(node.right)
            return node.val + leftG + rightG, max(leftF, leftG) + max(rightF, rightG)
        
        ans = dfs(root)
        return max(ans[0], ans[1])
