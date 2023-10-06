from algoexpert.TreeCreation import build_tree


def inOrderTraverse(tree, array):
    if tree is None:
        return
    postOrderTraverse(tree.left, array)
    array.append(tree.value)
    postOrderTraverse(tree.right, array)


def preOrderTraverse(tree, array):
    if tree is None:
        return
    array.append(tree.value)
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)


def postOrderTraverse(tree, array):
    if tree is None:
        return
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)

if __name__ == '__main__':
    tree1 = build_tree({
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": None, "right": "22", "value": 15},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": None, "value": 2},
            {"id": "1", "left": None, "right": None, "value": 1}
        ],
        "root": "10"
    })
    arr = []
    postOrderTraverse(tree1, arr)
    print(arr)