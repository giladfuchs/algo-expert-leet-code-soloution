def rightSmallerThanON2(array):
    res = []
    for i, num in enumerate(array):
        count = 0
        for j in range(i + 1, len(array)):
            if num > array[j]: count += 1
        res.append(count)
    return res


def rightSmallerThan(array):
    n = len(array) - 1
    print(array)
    print(sorted(array,  reverse=True))
    index_dict = {num: i for i, num in enumerate(sorted(array, reverse=True))}
    print(index_dict)
    res = [n - i - index_dict[num] for i, num in enumerate(array)]
    return res


if __name__ == '__main__':
    print(rightSmallerThan([8, 5, 11, -1, 3, 4, 2]))
