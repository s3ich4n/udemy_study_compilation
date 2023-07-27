import collections
from typing import Optional, Dict, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        ...


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)

root2 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(7)

s = Solution()
print(s.mergeTrees(root1, root2))
