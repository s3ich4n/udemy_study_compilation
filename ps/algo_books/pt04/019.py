from typing import Optional, Dict, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total: int = 0

    def tree_traversal(self, root: Optional[TreeNode]):
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0

            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)

            return

        dfs(root)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        BST에서, 자신보다 더 큰 값을 가진 모든 노드의 합
        BST이므로... 중위순회를 하면 된다
        (왜? 정렬된 순서대로 셀 수 있기 때문이다)
        어프로치 (1)
            1. 중위순회를 해서 모든 값을 다 구한다 -> 전체합 구하기
            2. 트리를 다시 타서, 자신보다 더 큰 값에 대한 연산을 진행한다
                1. 어떻게? - 빡세네 

        어프로치 (2)
            역으로 돌아버리면??????????? 처음부터 만들고 할 필요가 없이 바로할 수 있다.
            역으로 도는건 어케하는데? 우측-중앙-좌측 순으로의 중위순회만 하면됨.

            1. 역으로 돌면서 합을 계속 구한다
            2. 합을 넣는 변수와, 새로 구하는 변수를 함께 처리한다
                이 때, 기존 루트를 그대로 "덮어쓰면" 된다 
        """
        self.tree_traversal(root)

        return root


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)


s = Solution()
print(s.bstToGst(root))
