from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    __repr__ = __str__


def build_sll(*items):
    node = None
    for item in reversed(items):
        node = ListNode(val=item, next=node)
    return node


def safe_next(node: Optional[ListNode]) -> Optional[ListNode]:
    return node.next if node else node


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = safe_next(safe_next(safe_next(p1)))
            p2 = safe_next(p2)
        return p2


if __name__ == "__main__":
    solver = Solution()
    head = build_sll(1, 2, 3, 4, 5, 6)
    print(solver.middleNode(head=head))
