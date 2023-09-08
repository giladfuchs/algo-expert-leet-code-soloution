def minHeightBstHelp(array):
    # print(array)
    if not array:
        return None
    len_array = len(array)

    mid = len_array // 2
    root = BST(array[mid])
    if mid + 1 < len_array:
        root.right = minHeightBstHelp(array[mid:])

    if mid - 1 > 0:
        root.left = minHeightBstHelp(array[:mid])

    return root


def minHeightBst(array):
    root = minHeightBstHelp([-2] + array)
    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


a = minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])
a.insert(1)
print()
