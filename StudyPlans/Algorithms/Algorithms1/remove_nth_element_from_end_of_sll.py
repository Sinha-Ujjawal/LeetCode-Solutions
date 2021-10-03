from typing import Any, Iterable, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_sll(*items):
    node = None
    for item in reversed(items):
        node = ListNode(val=item, next=node)
    return node


def from_sll(head: Optional[ListNode]) -> Iterable[Any]:
    while head:
        yield head.val
        head = head.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        i = 0
        while p1 and i < n:
            p1 = p1.next
            i += 1
        prev, p2 = None, head
        while p1:
            p1 = p1.next
            prev, p2 = p2, p2.next
        if prev:
            prev.next = p2.next
        else:
            head = head.next
        return head


if __name__ == "__main__":
    solver = Solution()
    head = build_sll(1, 2, 3, 4, 5, 6)
    head = solver.removeNthFromEnd(head=head, n=2)
    print(list(from_sll(head)))
