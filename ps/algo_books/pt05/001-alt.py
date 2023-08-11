from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst = []

        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for idx in lst:
            p.val = idx
            p = p.next
        
        return p



root = ListNode(-1)
root.next = ListNode(5)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(0)

s = Solution()

s.sortList(root)

a = 1