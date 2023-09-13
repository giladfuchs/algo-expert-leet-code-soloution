from algoexpert.TreeCreation import build_tree  # , BinaryTree, tree_to_array


def pre_order_find(tree, target):
    def pre_order(node, next_stop=False):
        if node:

            if node.left:
                next_stop = pre_order(node.left, next_stop)
            # if next_stop:
            #     return node
            print(node.value)
            if node.value == target:
                next_stop = True
            if node.right:
                next_stop = pre_order(node.right, next_stop)
        return next_stop
    return pre_order(tree)


def findSuccessor(tree, node):
    in_order_arr = pre_order_find(tree, node)
    return in_order_arr


def run():
    tree1 = build_tree({
        "nodes": [
            {"id": "1", "left": "2", "parent": None, "right": "3", "value": 1},
            {"id": "2", "left": "4", "parent": "1", "right": "5", "value": 2},
            {"id": "3", "left": None, "parent": "1", "right": None, "value": 3},
            {"id": "4", "left": None, "parent": "2", "right": None, "value": 4},
            {"id": "5", "left": "6", "parent": "2", "right": "7", "value": 5},
            {"id": "6", "left": None, "parent": "5", "right": None, "value": 6},
            {"id": "7", "left": "8", "parent": "5", "right": None, "value": 7},
            {"id": "8", "left": None, "parent": "7", "right": None, "value": 8}
        ],
        "root": "1"
    }, )
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

    print(findSuccessor(tree1, 5).value)


if __name__ == '__main__':
    run()
