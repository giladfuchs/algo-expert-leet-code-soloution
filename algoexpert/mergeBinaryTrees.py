from algoexpert.TreeCreation import build_tree, BinaryTree


def mergeBinaryTrees(tree1, tree2):
    if not tree1 and not tree2:
        return None
    node = BinaryTree(((tree1 and tree1.value) or 0) + ((tree2 and tree2.value) or 0))
    node.left = mergeBinaryTrees(tree1 and tree1.left, tree2 and tree2.left)
    node.right = mergeBinaryTrees(tree1 and tree1.right, tree2 and tree2.right)

    return node


# from_solution
def sol_mergeBinaryTrees(tree1, tree2):
    if tree1 and tree2:
        root = BinaryTree(tree1.value + tree2.value)
        root.left = mergeBinaryTrees(tree1.left, tree2.left)
        root.right = mergeBinaryTrees(tree1.right, tree2.right)
        return root
    
    return tree1 or tree2


def run():
    tree1 = build_tree({
        "nodes": [
            {"id": "7", "left": None, "right": None, "value": 7}
        ],
        "root": "7"
    })
    tree2 = build_tree({
        "nodes": [
            {"id": "2", "left": "3", "right": "6", "value": 2},
            {"id": "3", "left": None, "right": "4", "value": 3},
            {"id": "6", "left": None, "right": "7", "value": 6},
            {"id": "4", "left": None, "right": None, "value": 4},
            {"id": "7", "left": None, "right": None, "value": 7}
        ],
        "root": "2"
    })
    a = mergeBinaryTrees(tree1, tree2)
    print()


if __name__ == '__main__':
    run()
