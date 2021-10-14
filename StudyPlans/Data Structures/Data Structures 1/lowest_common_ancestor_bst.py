from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    node = root
    while node:
        if val < node.val:
            node = node.left
        elif val > node.val:
            node = node.right
        else:
            break
    return node


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> Optional[TreeNode]:
        cur_node = root
        while cur_node:
            if (p.val <= cur_node.val <= q.val) or (p.val >= cur_node.val >= q.val):
                break
            elif p.val < cur_node.val and q.val < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        if search_bst(root, p.val) and search_bst(root, q.val):
            return cur_node


if __name__ == "__main__":
    solver = Solution()

    p = TreeNode(x=1)
    root = q = TreeNode(x=2)
    q.left = p

    print(solver.lowestCommonAncestor(root, p, q).val)
