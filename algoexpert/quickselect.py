def helper(array):
    pivot = array.pop()
    small = [_ for _ in array if _ <= pivot]
    big = [_ for _ in array if _ > pivot]
    return pivot, small, big


def quickselect(array, k):
    while True:
        pivot, small, big = helper(array)

        if len(small) == k - 1:
            return pivot
        if len(small) >= k:
            array = small
            if big:
                array += [pivot]
        else:
            array = [pivot] + big
            k -= len(small)


print(quickselect([8, 5, 2, 9, 7, 6, 3], 3))
