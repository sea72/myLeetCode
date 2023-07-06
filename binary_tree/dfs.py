from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root



class Solution:
    def preorderRecurveTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return [root.val] + self.preorderRecurveTraversal(root.left) + self.preorderRecurveTraversal(root.right)

    def inorderRecurveTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderRecurveTraversal(root.left) + [root.val] + self.inorderRecurveTraversal(root.right)

    def postorderRecurveTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderRecurveTraversal(root.left) + self.postorderRecurveTraversal(root.right) + [root.val]

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        curr = root
        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return res


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if not curr.right or prev == curr.right:
                curr = stack.pop()
                res.append(curr.val)
                prev = curr
                curr = None
            else:
                curr = curr.right
        return res
        #     root = stack.pop()
        #     # 每个节点两次入栈出栈，第一次是为了找他的右子树，第二次是为了找他自己，即根节点
        #     # 若没有右子树，或者右子树已经遍历过，就可以添加这个根节点了
        #     # 注意要置root为None，表示其左右子树均已遍历，防止其继续向下遍历
        #     if not root.right or root.right == prev:
        #         res.append(root.val)
        #         prev = root
        #         root = None
        #     else:
        #         stack.append(root)
        #         root = root.right
        # return res


sol = Solution()
root = stringToTreeNode("[5,4,6,1,2,7,8]")
print(sol.preorderRecurveTraversal(root))
print(sol.inorderRecurveTraversal(root))
print(sol.postorderRecurveTraversal(root))
print('-' * 20)
print(sol.preorderTraversal(root))
print(sol.inorderTraversal(root))
print(sol.postorderTraversal(root))
