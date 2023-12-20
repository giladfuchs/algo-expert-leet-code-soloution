def firstDuplicateValue2(array):
    s = set()
    for _ in array:
        if _ in s:
            return _
        s.add(_)

    return -1


def firstDuplicateValue(array):
    for i in range(len(array)):
        index = abs(array[i])
        if array[index - 1] < 0:
            return index
        array[index - 1] *= -1
    return -1


print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
