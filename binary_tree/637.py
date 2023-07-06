from collections import deque
from typing import Optional, List
import statistics

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        myQue = deque([root])
        res = []
        while myQue:
            temp = []
            for _ in range(len(myQue)):
                it = myQue.popleft()
                temp.append(it.val)
                if it.left:
                    myQue.append(it.left)
                if it.right:
                    myQue.append(it.right)
            res.append(statistics.mean(temp))
        return res
                