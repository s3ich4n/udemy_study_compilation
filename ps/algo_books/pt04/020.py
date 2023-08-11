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
        어프로치(1)
        1. 중위순회 하면서 꺼내온 값이 low와 high 사이인지 비교한다
        2. 그 사이면 별도 변수에 저장해서 끝내기
        """
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0

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
