from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        CALL = 0
        HANDLE = 1
        call_stack = [(CALL, root)]
        result_stack = []
        while call_stack:
            action, data = call_stack.pop()
            if action == CALL:
                if data:
                    call_stack.append((HANDLE, None))
                    call_stack.append((CALL, data.right))
                    call_stack.append((CALL, data.left))
                else:
                    result_stack.append(0)
            else:
                depth_left = result_stack.pop()
                depth_right = result_stack.pop()
                result_stack.append(1 + max(depth_left, depth_right))
        return result_stack[-1]
