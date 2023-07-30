import sys
from typing import Optional, Dict, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.val}]"


class Solution:
    min_val = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        data = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            # print(node.val)
            if data and node.val - data[-1] < self.min_val:
                self.min_val = node.val - data[-1]
                data[-1] = node.val
            else:
                data.append(node.val)
            dfs(node.right)

            return

        dfs(root)
        return self.min_val


s = Solution()

# root1 = TreeNode(4)
# root1.left = TreeNode(2)
# root1.left.left = TreeNode(1)
# root1.left.right = TreeNode(3)
# root1.right = TreeNode(6)
# print(s.minDiffInBST(root1))

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(48)
root2.right.left = TreeNode(12)
root2.right.right = TreeNode(49)
print(s.minDiffInBST(root2))

# root3 = TreeNode(10)
# root3.left = TreeNode(4)
# root3.right = TreeNode(15)
# root3.left.left = TreeNode(1)
# root3.left.right = TreeNode(8)
# print(s.minDiffInBST(root3))
