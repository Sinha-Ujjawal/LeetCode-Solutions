class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root:
            frontier = [root]
            while frontier:
                new_frontier = []
                for i in range(len(frontier) - 1):
                    node = frontier[i]
                    node.next = frontier[i + 1]
                    if node.left:
                        new_frontier.append(node.left)
                        new_frontier.append(node.right)
                if frontier[-1].left:
                    new_frontier.append(frontier[-1].left)
                    new_frontier.append(frontier[-1].right)
                frontier = new_frontier
        return root
