def firstDuplicateValue(array):
    s = set()
    for _ in array:
        if _ in s:
            return _
        s.add(_)


    return -1

print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))