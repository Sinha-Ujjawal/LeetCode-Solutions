from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            CALL = 0
            HANDLE = 1
            stack = [(CALL, root)]
            while stack:
                action, data = stack.pop()
                if action == CALL:
                    stack.append((HANDLE, data.val))
                    if data.right:
                        stack.append((CALL, data.right))
                    if data.left:
                        stack.append((CALL, data.left))
                else:
                    yield data
