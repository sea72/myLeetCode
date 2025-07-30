from typing import Optional, List
from MyTreeBase import TreeNode, stringToTreeNode
from collections import Counter

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cnt[cur.val] += 1
            cur = cur.right
        res = cnt.most_common()
        no = 1
        while no < len(res):
            if res[no][1] == res[no-1][1]:
                no += 1
            else:
                break
        return [item[0] for item in res[:no]]


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def do(val):
            nonlocal prev, mostCnt, cnt, res
            if val == prev:
                cnt += 1
            else:
                cnt = 1
            prev = val
            if cnt > mostCnt:
                mostCnt = cnt
                res = [val]
            elif cnt == mostCnt:
                res.append(val)

        stack = []
        cur = root
        prev = None
        cnt = 0
        mostCnt = 0
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            do(cur.val)
            cur = cur.right
        return res


sol = Solution()
node = stringToTreeNode("[1,null,2,2]")
print(sol.findMode(node))
