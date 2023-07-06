from MyTreeBase import TreeNode, stringToTreeNode
from typing import Optional, List

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def findPath(cur, path):
            if cur:
                path.append(str(cur.val))
                if cur.left is None and cur.right is None:
                    res.append(path[:])
                else:
                    if cur.left:
                        findPath(cur.left, path)
                        path.pop()
                    if cur.right:
                        findPath(cur.right, path)
                        path.pop()
        
        path = []
        findPath(root, path)
        return ['->'.join(it) for it in res ]
    
class Solution:
    def binaryTreePaths(self, root):
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
    
class Solution:
    def binaryTreePaths(self, root):
        paths = []
        stack = []
        cur = root
        path = []
        while cur or stack:
            while cur:
                path.append(str(cur.val))
                stack.append((cur, path[:]))
                cur = cur.left
            cur, path = stack[-1][0], stack[-1][1]
            stack.pop()
            if not cur.left and not cur.right:
                paths.append(path[:])
            cur = cur.right
        return ['->'.join(it) for it in paths ]




# import collections
# class Solution:
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         paths = list()
#         if not root:
#             return paths

#         node_queue = collections.deque([root])
#         path_queue = collections.deque([str(root.val)])

#         while node_queue:
#             node = node_queue.popleft()
#             path = path_queue.popleft()

#             if not node.left and not node.right:
#                 paths.append(path)
#             else:
#                 if node.left:
#                     node_queue.append(node.left)
#                     path_queue.append(path + '->' + str(node.left.val))
                
#                 if node.right:
#                     node_queue.append(node.right)
#                     path_queue.append(path + '->' + str(node.right.val))
#         return paths


sol = Solution()
root = stringToTreeNode("[1,2]")
print(sol.binaryTreePaths(root))