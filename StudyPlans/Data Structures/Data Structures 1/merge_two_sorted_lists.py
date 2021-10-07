from typing import Any, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def append_at_end(
    head: Optional[ListNode], tail: Optional[ListNode], val: Any
) -> Tuple[ListNode, ListNode]:
    if tail == None:
        head = tail = ListNode(val=val)
    else:
        tail.next = tail = ListNode(val=val)
    return head, tail


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = tail = None

        while l1 or l2:
            if l1 and (not l2 or l1.val <= l2.val):
                head, tail = append_at_end(head, tail, l1.val)
                l1 = l1.next
            else:
                head, tail = append_at_end(head, tail, l2.val)
                l2 = l2.next

        return head
