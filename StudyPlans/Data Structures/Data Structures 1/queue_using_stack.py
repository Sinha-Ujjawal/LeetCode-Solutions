from typing import Optional


class MyQueue:
    def __init__(self):
        self._left = []
        self._right = []

    def _rebalance(self):
        right = self._right
        take = max(len(right) >> 1, 1)
        self._left = right[:take][::-1]
        self._right = right[take:]

    def push(self, x: int) -> None:
        self._right.append(x)

    def pop(self) -> Optional[int]:
        if not self._left:
            self._rebalance()
        return self._left.pop() if self._left else None

    def peek(self) -> Optional[int]:
        if not self._left:
            self._rebalance()
        return self._left[-1] if self._left else None

    def empty(self) -> bool:
        return (len(self._left) + len(self._right)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
