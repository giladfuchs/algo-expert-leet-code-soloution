# This is an input class. Do not edit.
from algoexpert.TreeCreation import build_tree


def helpHeightBalancedBinaryTree(tree, h, is_balanced):
    if tree is None:
        return h
    left = helpHeightBalancedBinaryTree(tree.left, h + 1, is_balanced)
    right = helpHeightBalancedBinaryTree(tree.right, h + 1, is_balanced)
    if abs(left - right) > 1:
        is_balanced[0] = False
    return max(left, right)


def heightBalancedBinaryTree2(tree):
    is_balanced = [True]
    helpHeightBalancedBinaryTree(tree, 0, is_balanced)
    return is_balanced


def getHeightTree(tree):
    if tree is None:
        return 0
    left = getHeightTree(tree.left)
    right = getHeightTree(tree.right)

    return max(left, right) + 1


def heightBalancedBinaryTree(tree):
    if tree is None:
        return True
    if not heightBalancedBinaryTree(tree.left) or not heightBalancedBinaryTree(tree.right):
        return False
    left = getHeightTree(tree.left)
    right = getHeightTree(tree.right)
    return abs(left - right) <= 1


if __name__ == '__main__':
    root = build_tree({
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": None, "right": "6", "value": 3},
            {"id": "4", "left": None, "right": None, "value": 4},
            {"id": "5", "left": "7", "right": "8", "value": 5},
            {"id": "6", "left": None, "right": None, "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": None, "value": 8}
        ],
        "root": "1"
    })
    print(heightBalancedBinaryTree(root))
