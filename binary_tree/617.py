from MyTreeBase import TreeNode
from typing import Optional

# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root1 and not root2:
#             return
#         if root1:
#             root1.val = self.value(root1) + self.value(root2)
#         else:
#             root1 = TreeNode(self.value(root1) + self.value(root2))
#         root1.left = self.mergeTrees( self.lchild(root1), self.lchild(root2))
#         root1.right = self.mergeTrees( self.rchild(root1), self.rchild(root2))
#         return root1
    
#     def value(self, node):
#         return node.val if node else 0
    
#     def lchild(self, node):
#         return node.left if node else None
    
#     def rchild(self, node):
#         return node.right if node else None
    

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1, r2):
            if not r1 or not r2:
                return r1 if r1 else r2
            r1.val += r2.val
            r1.left = dfs(r1.left, r2.left)
            r1.right = dfs(r1.right, r2.right)
            return r1
        return dfs(root1, root2)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        merged = TreeNode(t1.val + t2.val)
        queue = collections.deque([merged])
        queue1 = collections.deque([t1])
        queue2 = collections.deque([t2])

        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2

        return merged
