from typing import Any, Optional, Tuple, Iterable


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def iter_sll(l: Optional[ListNode]) -> Iterable[Any]:
    while l:
        yield l.val
        l = l.next


def build_sll_from_items(*items) -> Optional[ListNode]:
    head = tail = None

    for val in items:
        head, tail = append_at_end(head, tail, val)

    return head


def append_at_end(
    head: Optional[ListNode], tail: Optional[ListNode], val: Any
) -> Tuple[ListNode, ListNode]:
    if tail == None:
        head = tail = ListNode(val=val)
    else:
        tail.next = tail = ListNode(val=val)
    return head, tail


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_value = None
        new_head = new_tail = None
        for val in iter_sll(head):
            if val != prev_value:
                new_head, new_tail = append_at_end(new_head, new_tail, val)
                prev_value = val
        return new_head


if __name__ == "__main__":
    solver = Solution()
    head = build_sll_from_items(1, 1, 2)
    print(list(iter_sll(solver.deleteDuplicates(head=head))))
