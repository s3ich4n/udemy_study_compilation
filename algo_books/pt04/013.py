import collections
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

    def traversal(self, node: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        queue = collections.deque([node])

        while queue:
            v = queue.popleft()
            result.append(v.val)

            if v.left is not None:
                queue.append(v.left)

            if v.right is not None:
                queue.append(v.right)

        return result

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        # a = self.traversal(root)
        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

s = Solution()
print(s.invertTree(root))
