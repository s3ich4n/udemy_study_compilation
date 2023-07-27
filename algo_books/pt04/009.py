import collections

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.val}]"


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs():
            depth = 0
            queue = collections.deque([root])

            while queue:
                for idx in range(len(queue)):
                    v = queue.popleft()

                    if v.left is not None:
                        queue.append(v.left)

                    if v.right is not None:
                        queue.append(v.right)

                depth += 1

            return depth

        return bfs()


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# root = TreeNode(1)
# root.right = TreeNode(2)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)

s = Solution()

print(s.maxDepth(root))
