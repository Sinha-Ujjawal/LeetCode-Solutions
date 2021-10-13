from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> TreeNode:
        new_node = TreeNode(val=val)
        if root:
            cur_node, parent_node = root, None
            while cur_node:
                parent_node = cur_node
                if val < cur_node.val:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right
            assert parent_node is not None
            if val < parent_node.val:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            return root
        else:
            return new_node


class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> TreeNode:
        new_node = TreeNode(val=val)
        CALL, HANDLE = 0, 1
        LEFT, RIGHT = 0, 1
        call_stack = [(CALL, root)]
        return_stack = []
        while call_stack:
            action, data = call_stack.pop()
            if action == CALL:
                node = data
                if node:
                    if val < node.val:
                        call_stack.append((HANDLE, (node, LEFT)))
                        call_stack.append((CALL, node.left))
                    else:
                        call_stack.append((HANDLE, (node, RIGHT)))
                        call_stack.append((CALL, node.right))
                else:
                    return_stack.append(new_node)
            else:
                node, direction = data
                child = return_stack.pop()
                if direction == LEFT:
                    left, right = child, node.right
                else:
                    left, right = node.left, child
                return_stack.append(
                    TreeNode(
                        val=node.val,
                        left=left,
                        right=right,
                    )
                )
        return return_stack[-1]
