from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_at_summit(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    stack = [(root1, root2)]
    while stack:
        r1, r2 = stack.pop()
        if not ((r1 is None and r2 is None) or (r1 and r2 and r1.val == r2.val)):
            return False
        if r1 and r2:
            stack.append((r1.right, r2.right))
            stack.append((r1.left, r2.left))
    return True


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if is_at_summit(node, subRoot):
                return True
            elif node:
                stack.append(node.left)
                stack.append(node.right)
        return False
