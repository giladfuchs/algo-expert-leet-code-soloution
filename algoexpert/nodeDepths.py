def nodeDepths(root):
    def bfs(node, depth):
        if node is None:
            return depth
        return max(bfs(node.right, depth + 1), bfs(node.left, depth + 1))

    return bfs(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
