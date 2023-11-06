def helper(array):
    pivot = array.pop()
    small = [_ for _ in array if _ <= pivot]
    big = [_ for _ in array if _ > pivot]
    return pivot, small, big


def quickSort(array):
    if len(array) <= 1:
        return array
    pivot, small, big = helper(array)
    return quickSort(small) + [pivot] + quickSort(big)


if __name__ == '__main__':
    arr = [_ for _ in range(22)]
    import random
    random.shuffle(arr)
    print(quickSort(arr))