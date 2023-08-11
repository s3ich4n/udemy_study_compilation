import collections
import math
from typing import Optional, Dict, List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"[{self.val}]"


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        1. 순회하면서 전체 길이를 파악? (이번엔 순회 순서가 중요하다!)
            1. bfs가 아무래도 층별로 탐색하니, 훨씬 나아보인다
            2. 다만 어느 지점에 비어있는지도 표기해야한다
        2. # 으로 자식노드의 값이 none인걸 표기함

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "# #"

        data = ["#"]
        queue = collections.deque([root])

        while queue:
            for _ in range(len(queue)):
                v = queue.popleft()

                # 자신이 트리라면, 하위값을 전부 append
                if v:
                    queue.append(v.left)
                    queue.append(v.right)

                    data.append(str(v.val))

                # 자신이 None이니까 이를 표기
                else:
                    data.append("#")

        return " ".join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        1. 1부터 시작, 2씩 불리면서?
        2. 배열 순회에 대한 방안?

        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return None

        serialized_nodes = data.split()[1::]

        base_tree = TreeNode(serialized_nodes.pop(0))

        def make_left_tree():
            is_valid_value = serialized_nodes.pop(0)
            if is_valid_value == "#":
                return None
            else:
                return TreeNode(int(is_valid_value))

        def make_right_tree():
            is_valid_value = serialized_nodes.pop(0)
            if is_valid_value == "#":
                return None
            else:
                return TreeNode(int(is_valid_value))

        queue = collections.deque([base_tree])

        while queue:
            node = queue.popleft()

            if node:
                node.left = make_left_tree()
                queue.append(node.left)
                node.right = make_right_tree()
                queue.append(node.right)

        return base_tree

# Your Codec object will be instantiated and called as such:

# root = TreeNode(None)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))

a = 1
