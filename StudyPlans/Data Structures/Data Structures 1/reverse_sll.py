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


def cons(head: Optional[ListNode], val: Any) -> ListNode:
    if head == None:
        return ListNode(val=val)
    else:
        return ListNode(val=val, next=head)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        for val in iter_sll(l=head):
            new_head = cons(head=new_head, val=val)
        return new_head


if __name__ == "__main__":
    solver = Solution()
    head = build_sll_from_items(1, 2, 4, 10)
    print(list(iter_sll(solver.reverseList(head=head))))
