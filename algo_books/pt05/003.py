import sys

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(-sys.maxsize)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            #
            # tips!
            #
            # 우측항의 컨텍스트는 그대로임. 바뀌지 않는다.
            # 좌측항은 그떄그때 우측항의 컨텍스트를 이용하여 자신의 값을 바꾼다.
            # 좌측에서 우측 순으로 연산된다.
            # 좌측에 바뀐 값은 우측에서도 그대로 적용되어있다.
            # 이를테면...
            #   cur.next로 head 연산을 하면, cur.next는 head 객체다.
            #   head.next는 cur.next 의 컨텍스트를 그대로 head.next에 둔다.
            #   head = head.next는 코드대로 진행된다.
            #
            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 포인터의 위치를 처음으로 돌리기
            # 포인터 위치를 옮기고 찾는 비용을 줄이기 위함
            if head and cur.val > head.val:
                cur = parent

        return parent.next


root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)
# root.next.next.next.next = ListNode(0)

# root = ListNode(-1)
# root.next = ListNode(5)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)
# root.next.next.next.next = ListNode(0)

s = Solution()

s.insertionSortList(root)
