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
    total: int = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        어프로치(2)
        1. 중위순회하면서 가지치기하자.
            low나 high 밖의 값으로 순회하는걸 방지하자
        """
        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            if node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            else:
                dfs(node.left)
                if low <= node.val <= high:
                    self.total += node.val
                dfs(node.right)

            return

        dfs(root)
        return self.total


root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right = TreeNode(15)
root1.right.right = TreeNode(18)

root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.left.left.left = TreeNode(1)
root2.left.right.left = TreeNode(6)
root2.right = TreeNode(15)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(root1, low=7, high=15))
s.total = 0
print(s.rangeSumBST(root2, low=6, high=10))
