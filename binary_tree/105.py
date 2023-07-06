from MyTreeBase import TreeNode
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        separator_idx = inorder.index(root_val)

        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        preorder_left = preorder[1:len(inorder_left) + 1]
        preorder_right = preorder[len(inorder_left) + 1:]

        root.right = self.buildTree(preorder_right, inorder_right,)
        root.left = self.buildTree(preorder_left, inorder_left)

        return root
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        from collections import deque
        preorder = deque(preorder)
        def helper(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None
            
            nonlocal preorder
            root_val = preorder.popleft()
            root_index = inorder.index(root_val)

            root = TreeNode(root_val)
            root.left = helper(inorder_left, root_index)
            root.right = help(root_index+1, inorder_right)

        return helper(0, len(inorder))
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]

            # 重走前序遍历，建栈
            # inorder[inorderIndex]是从中序遍历中来的值，也即当前这个树的最左尽头，也即中序中 左根右的左
            # stack 表征此次向下建栈过程中经过的结点（不考虑输出顺序，只考虑dfs深度优先）
            
            # 如果栈顶节点并没有到达最左，那也就是仍要继续向左，继续dfs
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            
            # 如果到达最左，则下一次必定是往右，至于是那一个祖先节点的右子树，不知道
            # 只知道当前 先序遍历的 preorderVal 这个节点是一个右子树的节点
            else:
                # 既然之前都是一路向左子，那么我就一路回溯回去，此时中序和先序，因为是一路向左，两者分别是 左根， 根左
                # 二者的顺序完全是相反的
                # 直到中序遍历越过了要找的那个节点，进入了下一次向左遍历，并直接到达了当前进入的新分支的最左侧（由于中序遍历的性质决定的）
                # 则将 preorderVal 节点分配给 刚刚越过的那个公共遍历的节点做右子树
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root


sol = Solution()
sol.buildTree([3,9,8,5,4,10,20,15,7], [4,5,8,10,9,3,15,20,7])
