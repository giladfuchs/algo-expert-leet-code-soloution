from algoexpert.TreeCreation import BST


# global Index.val
# Index.val = 0
class Index:
    val = 0


def reconstructBst(preOrderTraversalValues ):

    def helper(lower, upper):
        if Index.val == len(preOrderTraversalValues):
            return None
        root_val = preOrderTraversalValues[Index.val]
        if root_val <= lower or root_val >= upper:
            return None
        Index.val += 1
        # elif node.value
        left = helper(lower, root_val)
        right = helper(root_val, upper)
        return BST(root_val, left, right)


    root = helper(float('-inf'), float('inf'))
    return root

if __name__ == '__main__':
    b = reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])
    print(b)
