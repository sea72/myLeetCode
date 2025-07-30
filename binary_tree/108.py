from typing import List, Optional
from MyTreeBase import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            rootVal = nums[len(nums)//2]
            root = TreeNode(rootVal)
            root.left = self.sortedArrayToBST(nums[:len(nums)//2])
            root.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
            return root
        else:
            return None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


sol = Solution()
res = sol.sortedArrayToBST([-10,-3,0,5,9])
print('h')
        