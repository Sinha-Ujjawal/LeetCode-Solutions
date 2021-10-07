from typing import Any, Optional, Tuple, Iterable

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def iter_sll(l: Optional[ListNode]) -> Iterable[Any]:
    while l:
        yield l.val
        l = l.next


def append_at_end(
    head: Optional[ListNode], tail: Optional[ListNode], val: Any
) -> Tuple[ListNode, ListNode]:
    if tail == None:
        head = tail = ListNode(val=val)
    else:
        tail.next = tail = ListNode(val=val)
    return head, tail


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = new_tail = None
        for x in iter_sll(head):
            if x != val:
                new_head, new_tail = append_at_end(new_head, new_tail, x)
        return new_head
