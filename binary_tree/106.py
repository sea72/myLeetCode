from MyTreeBase import TreeNode
from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None
            
            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]
 
            # 构造树的根是后序遍历提供的，而去掉一个根后再去取下一个根时，这个根来自于其双亲节点的右子树。
            # 即我是按照右子树的顺序去创造节点的

            # 构造右子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index - 1)

            return root
        
        # 建立（元素，下标）键值对的哈希表
        idx_map = { val:idx for idx, val in enumerate(inorder) } 
        return helper(0, len(inorder) - 1)
    
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
#         if not postorder:
#             return None

#         # 第二步: 后序遍历的最后一个就是当前的中间节点.
#         root_val = postorder[-1]
#         root = TreeNode(root_val)

#         # 第三步: 找切割点.
#         separator_idx = inorder.index(root_val)

#         # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
#         inorder_left = inorder[:separator_idx]
#         inorder_right = inorder[separator_idx + 1:]

#         # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
#         # 重点1: 中序数组大小一定跟后序数组大小是相同的.
#         postorder_left = postorder[:len(inorder_left)]
#         postorder_right = postorder[len(inorder_left): len(postorder) - 1]

#         # 第六步: 递归
#         root.right = self.buildTree(inorder_right, postorder_right)
#         root.left = self.buildTree(inorder_left, postorder_left)



#          # 第七步: 返回答案
#         return root
    
sol = Solution()
res = sol.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print('h')