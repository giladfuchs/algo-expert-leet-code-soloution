from algoexpert.TreeCreation import build_tree


global max_path
max_path = 0


def binaryTreeDiameter(tree):
    def help_binaryTreeDiameter(node):
        global max_path
        if node is None:
            return 0

        left_sum = help_binaryTreeDiameter(node.left)
        right_sum = help_binaryTreeDiameter(node.right)
        max_path = max(max_path, left_sum + right_sum)
        return max(left_sum, right_sum) + 1

    help_binaryTreeDiameter(tree)
    return max_path


if __name__ == '__main__':
    tree1 = build_tree({
        "nodes": [
            {"id": "1", "left": "3", "right": "2", "value": 1},
            {"id": "3", "left": "7", "right": "4", "value": 3},
            {"id": "7", "left": "8", "right": None, "value": 7},
            {"id": "8", "left": "9", "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "4", "left": None, "right": "5", "value": 4},
            {"id": "5", "left": None, "right": "6", "value": 5},
            {"id": "6", "left": None, "right": None, "value": 6},
            {"id": "2", "left": None, "right": None, "value": 2}
        ],
        "root": "1"
    })
    # AA.binaryTreeDiameter(node=tree1)
    print(binaryTreeDiameter(tree1))
    print(max_path)
    # print(AA.max_path)
