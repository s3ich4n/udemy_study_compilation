from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def __init__(self):
#             self.diameter = 0

#         def dfs(leaf: Optional[TreeNode], depth: int):
#             if leaf.left:
#                 dfs(leaf.left, depth + 1)
#                 dfs(leaf.right, depth + 1)

#             if leaf.right:
#                 dfs(leaf.left, depth + 1)
#                 dfs(leaf.right, depth + 1)

#             return depth

#         return dfs(root, depth=0)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def __init__(self):
            self.longest = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)  # 양쪽 상태값의 합에 + 2
            return max(left, right) + 1

        dfs(root)
        return self.longest


# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = None
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(1)
# root.left.right.left = TreeNode(5)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(root))
