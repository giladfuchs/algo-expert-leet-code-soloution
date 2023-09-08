from algoexpert.TreeCreation import build_tree, tree_to_array


def symmetricalTree(tree):
    pre = tree_to_array(tree.left, in_order=True)
    post = tree_to_array(tree.right,   post_order=True)
    return pre == post[::-1]


if __name__ == '__main__':
    root = build_tree({
        "nodes": [
            {"id": "1", "left": "2", "right": "2-2", "value": 1},
            {"id": "2", "left": "3", "right": "4", "value": 2},
            {"id": "2-2", "left": "4-2", "right": "3-2", "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3},
            {"id": "3-2", "left": None, "right": None, "value": 3},
            {"id": "4", "left": "5-2", "right": None, "value": 4},
            {"id": "4-2", "left": None, "right": "5", "value": 4},
            {"id": "5", "left": None, "right": None, "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5}
        ],
        "root": "1"
    })
    print(symmetricalTree(root))
