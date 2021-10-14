from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        CALL, HANDLE = 0, 1
        call_stack = [(CALL, root)]
        prev = None
        while call_stack:
            action, node = call_stack.pop()
            if action == CALL:
                if node:
                    call_stack.append((CALL, node.right))
                    call_stack.append((HANDLE, node))
                    call_stack.append((CALL, node.left))
            else:
                if prev is not None and prev > node.val:
                    return False
                prev = node.val
        return True
