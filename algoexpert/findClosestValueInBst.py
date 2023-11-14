

def findClosestValueInBst(tree, target):
    def find_close(node, res):
        if node is None:
            return res
        if abs(target - res.value) > abs(target - node.value):
            res = node
        res = find_close(node.left, res)
        res = find_close(node.right, res)

        return res

    ans = tree
    ans = find_close(tree, ans)
    return ans

if __name__ == '__main__':
    from algoexpert.TreeCreation import build_tree

    tree1 = build_tree({
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "13", "left": None, "right": "14", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": None, "value": 2},
            {"id": "1", "left": None, "right": None, "value": 1}
        ],
        "root": "10"
    })
    a = findClosestValueInBst(tree1, 12)
    print()
