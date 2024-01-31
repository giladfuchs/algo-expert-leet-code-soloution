# Represents a node of an n-ary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.child = []


# Level order traversal of the tree, returning a list of lists
def LevelOrderTraversal(root: Node):
    if root is None:
        return []

    result = []  # List to hold the result (list of lists)
    queue = [root]  # Create a queue and enqueue the root node

    while queue:
        level_nodes = []  # List to hold nodes at the current level

        # Process all nodes at the current level
        for _ in range(len(queue)):
            node = queue.pop(0)
            level_nodes.append(node.key)  # Append node key to current level list

            # Enqueue children of the current node
            for child in node.child:
                queue.append(child)

        result.append(sorted(level_nodes))  # Append the list of current level nodes to the result list

    return result


# Driver program
if __name__ == '__main__':
    ''' Let us create below tree
                10
            / / \ \
            2 34 56 100
        / \         | / | \
        77 88     1 7 8 9
    '''
    _root = Node(10)
    _root.child.append(Node(2))
    _root.child.append(Node(34))
    _root.child.append(Node(56))
    _root.child.append(Node(100))
    _root.child[0].child.append(Node(77))
    _root.child[0].child.append(Node(88))
    _root.child[2].child.append(Node(1))
    _root.child[3].child.append(Node(7))
    _root.child[3].child.append(Node(8))
    _root.child[3].child.append(Node(9))

    print("Level order traversal:")
    levels = LevelOrderTraversal(_root)
    for i, level in enumerate(levels):
        print(f"Level {i + 1}: {level}")
