from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            CALL = 0
            HANDLE = 1
            call_stack = [(CALL, (root.left, root.right))]
            result_stack = []
            while call_stack:
                action, data = call_stack.pop()
                nl, nr = data
                if action == CALL:
                    if nl and nr:
                        call_stack.append((HANDLE, (nl, nr)))
                        call_stack.append((CALL, (nl.right, nr.left)))
                        call_stack.append((CALL, (nl.left, nr.right)))
                    elif nl == None and nr == None:
                        result_stack.append(True)
                    else:
                        return False
                else:
                    check_left = result_stack.pop()
                    check_right = result_stack.pop()
                    res = check_left and check_right and nl.val == nr.val
                    if res:
                        result_stack.append(res)
                    else:
                        return False
            return True
        else:
            return False
