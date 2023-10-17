def make_subsets(arr, res, subset=[], index=0):
    res.append(subset[:])
    for i in range(index, len(arr)):
        subset.append(arr[i])
        make_subsets(arr, res, subset, i + 1)
        subset.pop()


if __name__ == '__main__':
    sets = []
    make_subsets(list(range(3)), sets)
    print(sets)
