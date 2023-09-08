# This is an input class. Do not edit.
from algoexpert.TreeCreation import build_tree


def getTreeSum(tree):
    return 0 if tree is None else \
        tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)


def trySubTrees(tree, desired_sub_tree_sum):
    if tree is None:
        return 0, False
    left_sum, left_can_be_split = trySubTrees(tree.left, desired_sub_tree_sum)
    right_sum, right_can_be_split = trySubTrees(tree.right, desired_sub_tree_sum)
    current_tree_sum = tree.value + left_sum + right_sum
    can_be_split = left_can_be_split or right_can_be_split or desired_sub_tree_sum == current_tree_sum
    return current_tree_sum, can_be_split


def splitBinaryTree(tree):
    desired_sub_tree_sum = getTreeSum(tree) // 2
    can_be_split = trySubTrees(tree, desired_sub_tree_sum)[1]
    # Write your code here.
    return desired_sub_tree_sum if can_be_split else 0

# copy solution
def run():
    tree1 = build_tree({
        "nodes": [
            {"id": "7", "left": None, "right": None, "value": 7}
        ],
        "root": "7"
    })
    tree2 = build_tree({
        "nodes": [
            {"id": "1", "left": "3", "right": "2", "value": 1},
            {"id": "2", "left": None, "right": "-5", "value": 2},
            {"id": "3", "left": "12", "right": None, "value": 1},
            {"id": "12", "left": None, "right": "-21", "value": 12},
            {"id": "-21", "left": None, "right": None, "value": -21},
            {"id": "-5", "left": None, "right": None, "value": -5}
        ],
        "root": "1"
    })

    print(splitBinaryTree(tree2))


if __name__ == '__main__':
    run()
