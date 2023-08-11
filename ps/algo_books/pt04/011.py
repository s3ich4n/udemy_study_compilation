from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.val}]"


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def iterative_dfs(node: Optional[TreeNode]):
#             depth = 0
#             queue = collections.deque([node])

#             if node is None:
#                 return 0

#             while queue:
#                 for idx in range(len(queue)):
#                     v = queue.popleft()

#                     if v.left is not None:
#                         queue.append(v.left)

#                     if v.right is not None:
#                         queue.append(v.right)
                
#                 depth += 1
            
#             return depth

#         left = iterative_dfs(root.left)
#         right = iterative_dfs(root.right)

#         return left + right


# class Solution:
#     longest: int = 0

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def dfs(node: Optional[TreeNode], result: int = 0):
#             if node.left is not None:
#                 result_left = dfs(node.left)
            
#             if node.right is not None:
#                 result_right = dfs(node.right)

#             return max(result_left + result_right)

#         left = dfs(root.left)
#         right = dfs(root.right)

#         return left + right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return -1
        
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)

        return self.longest


# [37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]
# root = TreeNode(37)
# root.left = TreeNode(-34)
# root.left.right = TreeNode(-100)
# ###
# root.right = TreeNode(-48)
# root.right.left = TreeNode(-100)
# root.right.right = TreeNode(48)
# root.right.right.left = TreeNode(-54)
# root.right.right.left.left = TreeNode(-71)
# root.right.right.left.right = TreeNode(-22)
# root.right.right.left.right.right = TreeNode(8)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)
root.right.left.right.left = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.right.left.left = TreeNode(10)

s = Solution()
print(s.diameterOfBinaryTree(root))
