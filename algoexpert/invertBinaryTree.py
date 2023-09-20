from algoexpert.TreeCreation import build_tree, BinaryTree, print_tree


def helpInvertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return None
    root = BinaryTree(tree.value)
    root.left = helpInvertBinaryTree(tree.right)
    root.right = helpInvertBinaryTree(tree.left)

    return root

def invertBinaryTree(tree):
    if tree is None:
        return None
    tree.left, tree.right = invertBinaryTree(tree.right), invertBinaryTree(tree.left)

    return tree


if __name__ == '__main__':
    _root = build_tree({
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "5", "left": None, "right": None, "value": 5},
            {"id": "6", "left": None, "right": None, "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9}
        ],
        "root": "1"
    })
    print_tree(_root)
    a = invertBinaryTree(_root)
    print_tree(a)
    print()
