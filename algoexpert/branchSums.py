def branchSums(root):
    if root is None:
        return []
    nodes = branchSums(root.left) + branchSums(root.right)
    return [x + root.value for x in nodes] if nodes else [root.value]
