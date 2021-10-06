from typing import Any, Iterable, Optional, Tuple


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


def build_sll_from_items(*items) -> Optional[ListNode]:
    head = tail = None

    for val in items:
        head, tail = append_at_end(head, tail, val)

    return head


def iter_sll(l: Optional[ListNode]) -> Iterable[Any]:
    while l:
        yield l.val
        l = l.next


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


if __name__ == "__main__":
    solver = Solution()
    l1 = build_sll_from_items(1, 2, 4, 10)
    l2 = build_sll_from_items(1, 3, 4, 100, 111)
    print(list(iter_sll(solver.mergeTwoLists(l1=l1, l2=l2))))
