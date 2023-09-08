from algoexpert.TreeCreation import build_tree, print_tree, tree_to_array


def validateBst(tree):
    # Write your code here.
    lst = tree_to_array(tree, pre_order=True)
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))





if __name__ == '__main__':
    root = build_tree( {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": None, "right": None, "value": 15},
        {"id": "5", "left": None, "right": "10-2", "value": 5},
        {"id": "10-2", "left": None, "right": None, "value": 10}
    ],
    "root": "10"
  } )
    print_tree(root)

    print(validateBst(root))