class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.len = 0

    def __len__(self) -> int:
        return self.len

    # O(1)
    def insert_head(self, data):
        self.len += 1
        new_node = Node(data)

        # 헤드가 없으면?
        if self.head is None:
            self.head = new_node
        # 기존 헤더가 있으면?
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_tail(self, data):
        self.len += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            cur_node = self.head

            while cur_node.next is not None:
                cur_node = cur_node.next

            cur_node.next = new_node

    def traverse(self):
        cur_node = self.head

        while cur_node:
            print(cur_node)
            cur_node = cur_node.next

    def get_middle_node(self):
        fast_ptr = self.head
        slow_ptr = self.head

        while fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr

    def remove(self, data):
        if self.head is None:
            return

        cur_node = self.head
        prev_node = None

        while cur_node and cur_node.data != data:
            prev_node, cur_node = cur_node, cur_node.next

        if cur_node is None:
            return

        if prev_node is None:
            self.head = cur_node.next
            self.len -= 1
        else:
            prev_node.next = cur_node.next
            self.len -= 1


linked_list = LinkedList()
linked_list.insert_head(10)
linked_list.insert_head('two')
linked_list.insert_head(3.14)
linked_list.insert_head(444)
linked_list.insert_head(555)
linked_list.insert_head(6)
linked_list.traverse()
print('----------')
print(linked_list.get_middle_node().data)
