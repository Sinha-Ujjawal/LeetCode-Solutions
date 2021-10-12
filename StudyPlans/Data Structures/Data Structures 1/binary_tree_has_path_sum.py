from typing import Optional

#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            stack = [(root, 0)]
            while stack:
                node, s = stack.pop()
                new_s = s + node.val
                if new_s == targetSum and (not (node.left or node.right)):
                    return True
                if node.left:
                    stack.append((node.left, new_s))
                if node.right:
                    stack.append((node.right, new_s))
        return False
