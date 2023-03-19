class Node:
    def __init__(
            self,
            data,
            parent,
    ) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0


class AVLTree:

    def __init__(self) -> None:
        # 루트에 명시적으로 접근가능.
        self.root = None

    def remove(self, data):
        if self.remove:
            self._remove_node(data, self.root)

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)

        else:
            self._insert_node(data, self.root)

    def _insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self._insert_node(data, node.left)

            else:
                node.left = Node(data, node)
                node.height = 1 + max(
                    self.calc_height(node.left),
                    self.calc_height(node.right),
                )

        elif data > node.data:
            if node.right:
                self._insert_node(data, node.right)

            else:
                node.right = Node(data, node)
                node.height = 1 + max(
                    self.calc_height(node.left),
                    self.calc_height(node.right),
                )

        # 노드가 균형이 맞는지 "항상" 살펴봐야함.
        self.handle_violation(node)

    def _remove_node(self, data, node):
        if not node:
            return

        if data < node.data:
            self._remove_node(data, node.left)

        elif data > node.data:
            self._remove_node(data, node.right)

        else:
            # case 1) 리프노드를 지우는 경우
            if node.left is None and node.right is None:
                print(f"removing a leaf node... {node.data}")
                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = None

                if parent is not None and parent.right == node:
                    parent.right = None

                if parent is None:
                    self.root = None

                del node

                # 노드가 균형이 맞는지 "항상" 살펴봐야함.
                self.handle_violation(parent)

            # case 2) "우측" 자식이 있는 경우?
            elif node.left is None and node.right is not None:
                print(
                    f"removing a node with single right child... {node.data}"
                )
                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right = node.right
                else:
                    self.root = node.right

                node.right.parent = parent
                del node

                # 노드가 균형이 맞는지 "항상" 살펴봐야함.
                self.handle_violation(parent)

            # case 3) "좌측" 자식이 있는 경우?
            elif node.right is None and node.left is not None:
                print(
                    f"removing a node with single left child... {node.data}"
                )
                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                else:
                    self.root = node.left

                node.left.parent = parent
                del node

                # 노드가 균형이 맞는지 "항상" 살펴봐야함.
                self.handle_violation(parent)

            # case 4) 노드가 두 자식을 가지는 경우... LR, RL 등을 재귀로 쫓아가야함.
            else:
                print("removing node with two children... ")

                predecessor = self._get_predecessor(node.left)
                predecessor.data, node.data = node.data, predecessor.data

                self._remove_node(data, predecessor)

    def _get_predecessor(self, node):
        if node.right:
            return self._get_predecessor(node.right)

        return node

    def violation_helper(self, node):
        balance = self.calculate_balance(node)

        # 좌측에 쏠린 경우
        if balance > 1:
            # LR
            if self.calculate_balance(node.left) < 0:
                self.rotate_left(node.left)

            # LL
            self.rotate_right(node)

        # 우측에 쏠린 경우
        if balance < -1:
            # RL
            if self.calculate_balance(node.right) > 0:
                self.rotate_right(node.right)

            # RR
            self.rotate_left(node)

    def calc_height(self, node):
        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0

        return self.calc_height(node.left) - self.calc_height(node.right)

    def handle_violation(self, node):
        """ 노드 삽입/삭제 후 점검
        """
        while node is not None:
            node.height = 1 + max(self.calc_height(node.left),
                                  self.calc_height(node.right))
            self.violation_helper(node)

            node = node.parent

    def rotate_left(self, node):
        print(f"rotating to the left on node: {node.data}")

        # 회전 로직
        temp_right_node = node.right
        t = temp_right_node.left

        temp_right_node.left = node
        node.right = t

        if t is not None:
            t.parent = None

        # 부모노드 처리 로직
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left == node:
            temp_right_node.parent.left = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right == node:
            temp_right_node.parent.right = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        # 높이값 보정
        node.height = max(self.calc_height(node.left),
                          self.calc_height(node.right))

        temp_right_node.height = 1 + max(self.calc_height(node.left),
                                         self.calc_height(node.right))

    def rotate_right(self, node):
        print(f"rotating to the right on node: {node.data}")

        # 회전 로직
        temp_left_node = node.left
        t = temp_left_node.right

        temp_left_node.right = node
        node.left = t

        if t is not None:
            t.parent = None

        # 부모노드 처리 로직
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left == node:
            temp_left_node.parent.left = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right == node:
            temp_left_node.parent.right = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        # 높이값 보정
        node.height = max(self.calc_height(node.left),
                          self.calc_height(node.right))

        temp_left_node.height = 1 + max(self.calc_height(node.left),
                                        self.calc_height(node.right))

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)

        l = ''
        r = ''
        p = ''

        if node.left is not None:
            l = node.left.data
        else:
            l = 'NULL'

        if node.right is not None:
            r = node.right.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print("%s left: %s right: %s parent: %s height: %s" %
              (node.data, l, r, p, node.height))

        if node.right:
            self.traverse_in_order(node.right)


if __name__ == "__main__":
    avl = AVLTree()

    avl.insert(15)
    avl.insert(13)
    avl.insert(16)
    avl.insert(10)
    avl.insert(19)
    avl.insert(22)
    avl.insert(17)
    avl.insert(9)
    avl.insert(6)
    avl.insert(23)
    avl.insert(25)
    avl.insert(1)

    avl.remove(6)

    avl.traverse()
