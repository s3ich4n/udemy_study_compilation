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
    def buildTree(
            self,
            preorder: List[int],
            inorder: List[int],
    ) -> Optional[TreeNode]:
        """
        어프로치 (1)
        1. 전위순회하면 어떻게 나옴? -
        2. 중위순회하면 어떻게 나옴? -
        """
        root = TreeNode(preorder[0])

        def tree(
                node: Optional[TreeNode],
                split_preorder: List[int],
                split_inorder: List[int],
        ):
            if not split_inorder:
                return

            idx_inorder = split_inorder.index(split_preorder.pop(0))
            left_inorder = split_inorder[0:idx_inorder]
            right_inorder = split_inorder[idx_inorder + 1:]

            node = TreeNode(split_inorder[idx_inorder])

            node.left = tree(
                node,
                split_preorder,
                left_inorder,
            )
            node.right = tree(
                node,
                split_preorder,
                right_inorder,
            )

            return node

        idx_inorder = inorder.index(preorder.pop(0))
        left_inorder = inorder[0:idx_inorder]
        right_inorder = inorder[idx_inorder + 1:]

        root.left = tree(
            root,
            preorder,
            left_inorder,
        )
        root.right = tree(
            root,
            preorder,
            right_inorder,
        )

        return root


s = Solution()
a = s.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
# b = s.buildTree(preorder=[-1], inorder=[-1])
c = s.buildTree(preorder=[1,2,3], inorder=[2,3,1])
d = 1
# def preorder(node):
#     if not node:
#         return

#     print(node.val)
#     preorder(node.left)
#     preorder(node.right)

#     return


# def inorder(node):
#     if not node:
#         return

#     inorder(node.left)
#     print(node.val)
#     inorder(node.right)

#     return


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# preorder(root)
# print("--------------")
# inorder(root)
