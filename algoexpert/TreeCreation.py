# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree(BST):
    def insert(self, num):
        if num <= self.value:
            if self.left is not None:
                self.left.insert(num)
            else:
                self.left = BinaryTree(num)
        else:
            if self.right is not None:
                self.right.insert(num)
            else:
                self.right = BinaryTree(num)


def array_to_binary_tree(array: list):
    if not array:
        return None
    root = BST(array.pop(0))

    return root


def find_by_id(nodes, _id):
    return next((_ for _ in nodes if _.get('id') == _id), None)


def create_tree(nodes, _id):
    node_data = find_by_id(nodes, _id)
    if node_data is None:
        return None
    node = BST(value=node_data.get('value'))
    node.right = create_tree(nodes, node_data.get('right'))
    node.left = create_tree(nodes, node_data.get('left'))
    return node


def build_tree(data):
    root = create_tree(data["nodes"], data["root"])

    return root


def tree_to_array(tree, pre_order=False, in_order=False, post_order=False):
    res = []

    def make_array(node):
        if node:
            if in_order:
                res.append(node.value)
            if node.left:
                make_array(node.left)
            if pre_order:
                res.append(node.value)
            if node.right:
                make_array(node.right)

            if post_order:
                res.append(node.value)

    make_array(tree)
    return res


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")
