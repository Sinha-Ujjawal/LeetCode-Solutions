from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        CALL = 0
        HANDLE = 1
        call_stack = [(CALL, root)]
        result_stack = []
        while call_stack:
            action, data = call_stack.pop()
            node = data
            if action == CALL:
                if node:
                    call_stack.append((HANDLE, node))
                    call_stack.append((CALL, node.right))
                    call_stack.append((CALL, node.left))
                else:
                    result_stack.append(None)
            else:
                right_node = result_stack.pop()
                left_node = result_stack.pop()
                result_stack.append(
                    TreeNode(
                        val=node.val,
                        left=right_node,
                        right=left_node,
                    )
                )
        return result_stack[-1]
