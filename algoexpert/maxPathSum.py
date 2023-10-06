from algoexpert.TreeCreation import build_tree


def findMaxSum(tree):
    if tree is None:
        return 0, 0
    left_max_sum_as_branch, left_max_path_sum = findMaxSum(tree.left)
    right_max_sum_as_branch, right_max_path_sum = findMaxSum(tree.right)
    max_child_sum_as_branch = max(left_max_sum_as_branch, right_max_sum_as_branch)
    val = tree.value
    max_sum_as_branch = max(max_child_sum_as_branch + val, val)
    max_sum_as_root = max(left_max_sum_as_branch + right_max_sum_as_branch + val, max_sum_as_branch)
    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_as_root)
    return max_sum_as_branch, max_path_sum


def maxPathSum(tree):
    _, max_sum = findMaxSum(tree)
    return max_sum


if __name__ == '__main__':
    tree1 = build_tree({
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "6", "left": None, "right": None, "value": 6},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "5", "left": None, "right": None, "value": 5},
            {"id": "4", "left": None, "right": None, "value": 4}
        ],
        "root": "1"
    })

    print(maxPathSum(tree1))
