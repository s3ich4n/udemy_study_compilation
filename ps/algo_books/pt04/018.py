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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        정렬된 값이므로, 중앙에서부터 반씩 나눠서 재귀를 수행
        하면서 계속 좌우의 값을 넣어줌
            투 포인터도 필요없고 재커하면 됨
        """
        if not nums:
            return TreeNode()

        def tree(node: Optional[TreeNode], split_nums: List[int]):
            if len(split_nums) < 1:
                return

            mid = split_nums[len(split_nums) // 2]

            if len(split_nums) == 1:
                return TreeNode(mid)

            leaf = TreeNode(mid)
            leaf.left = tree(leaf.left, split_nums[:len(split_nums) // 2])
            leaf.right = tree(leaf.right, split_nums[(len(split_nums) // 2) + 1:])

            return leaf

        root = TreeNode(nums[len(nums) // 2])

        root.left = tree(root.left, nums[:len(nums) // 2])
        root.right = tree(root.right, nums[(len(nums) // 2) + 1:])

        return root


s = Solution()
# a = s.sortedArrayToBST(nums=[-10,3,0,5,9])
b = s.sortedArrayToBST(nums=[1,3])

z = 1