# This is an input class. Do not edit.
from algoexpert.TreeCreation import build_tree


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst_with_array(tree, k):
    # Write your code here.
    arr = []

    def create_arr(node):
        if node is not None:
            if node.left is not None:
                create_arr(node.left)
            arr.append(node.value)
            if node.right is not None:
                create_arr(node.right)

    create_arr(tree)

    return arr[-k]


def reverseInOrder(node, k, info):
    if node is None or k <= info["count_visit"]:
        return
    reverseInOrder(node.right, k, info)
    if info["count_visit"] < k:
        info["count_visit"] += 1
        info['last_visit'] = node.value
        reverseInOrder(node.left, k, info)


def findKthLargestValueInBst(tree, k):
    info = dict(last_visit=-1, count_visit=0)

    reverseInOrder(tree, k, info)
    return info['last_visit']


def find_by_id(nodes, _id):
    return next((_ for _ in nodes if _.get('id') == _id), None)


if __name__ == '__main__':
    root = build_tree(data={
        "nodes": [
            {"id": "15", "left": "5", "right": "20", "value": 15},
            {"id": "20", "left": "17", "right": "22", "value": 20},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "17", "left": None, "right": None, "value": 17},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": "3", "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3},
            {"id": "1", "left": None, "right": None, "value": 1}
        ],
        "root": "15"
    })
    print(findKthLargestValueInBst(root, 3))
