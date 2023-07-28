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
    new_tree = TreeNode()

    def get_merged_value(
            self,
            left: Optional[TreeNode],
            right: Optional[TreeNode],
    ):
        tree = TreeNode()
        if left is not None:
            tree.val += left.val

        if right is not None:
            tree.val += right.val

        return tree

    def mergeTrees(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        def dfs(
                node1: Optional[TreeNode],
                node2: Optional[TreeNode],
        ):
            if node1 and node2:
                tree = self.get_merged_value(node1, node2)

                tree.left = dfs(node1.left, node2.left)
                tree.right = dfs(node1.right, node2.right)

                return tree

            # 자식 노드에 아무것도 존재하지 않을 때
            if node1 is None and node2 is None:
                return

            # 한쪽 노드만 존재해서, 그쪽만 리턴하면 될 때
            if node1 is None or node2 is None:
                return node1 or node2

        self.new_tree = dfs(root1, root2)

        return self.new_tree

    def tree_traversal(self, root: Optional[TreeNode],):
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            print(node.val)

            return
    
        dfs(root)


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.left.left = TreeNode(3)

# root2 = TreeNode(1)
# root2.right = TreeNode(2)
# root2.right.right = TreeNode(3)

s = Solution()
new_tree = s.mergeTrees(root1, root2)
s.tree_traversal(new_tree)
