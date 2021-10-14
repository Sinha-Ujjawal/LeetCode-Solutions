from typing import Any, Iterable, Optional, Tuple
from itertools import chain

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def append_at_end(
    head: Optional[ListNode],
    tail: Optional[ListNode],
    val: Any,
) -> Tuple[ListNode, ListNode]:
    if not tail:
        head = tail = ListNode(val=val)
    else:
        tail.next = ListNode(val=val)
        tail = tail.next
    return head, tail


def iter_sll(head: Optional[ListNode]) -> Iterable[Any]:
    while head:
        yield head.val
        head = head.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = new_tail = prev = None
        duplicate = False
        for val in chain(iter_sll(head), [None]):
            if val != prev:
                if prev is not None and not duplicate:
                    new_head, new_tail = append_at_end(new_head, new_tail, prev)
                prev = val
                duplicate = False
            else:
                duplicate = True
        return new_head
