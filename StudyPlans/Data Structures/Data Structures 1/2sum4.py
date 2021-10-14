from typing import Any, Iterable, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iter_tree(root: Optional[TreeNode]) -> Iterable[Any]:
    CALL, HANDLE = 0, 1
    call_stack = [(CALL, root)]
    while call_stack:
        action, node = call_stack.pop()
        if action == CALL:
            if node:
                if node.right:
                    call_stack.append((CALL, node.right))
                call_stack.append((HANDLE, node))
                if node.left:
                    call_stack.append((CALL, node.left))
        else:
            yield node.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = list(iter_tree(root))
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                i += 1
            elif s > k:
                j -= 1
            else:
                return True
        return False
