from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        valueLoc = { nums[i]: i for i in range(len(nums))}
        def makeNode(start, end):
            if start > end:
                return
            maxValue = max(nums[start:end+1])
            maxLoc = valueLoc[maxValue]
            root = TreeNode(maxValue)
            root.left = makeNode(start, maxLoc-1)
            root.right = makeNode(maxLoc+1, end)
            return root
        return makeNode(0, len(nums)-1)
    


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

    


