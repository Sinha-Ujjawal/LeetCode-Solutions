from typing import Iterable, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> Iterable[List[int]]:
        ans = []
        if root:
            frontier = [root]
            while frontier:
                new_frontier = []
                for node in frontier:
                    if node.left:
                        new_frontier.append(node.left)
                    if node.right:
                        new_frontier.append(node.right)
                yield [node.val for node in frontier]
                frontier = new_frontier
