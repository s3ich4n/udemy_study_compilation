import collections
from typing import Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.val}]"


class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0

            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.longest = max(self.longest, left + right)
            return max(left, right)

        dfs(root)

        return self.longest


# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(1)
# root.right.right = TreeNode(5)

# root = TreeNode(5)
# root.left = TreeNode(5)
# root.right = TreeNode(5)

root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(5)

s = Solution()
print(s.longestUnivaluePath(root))
