def minOrMaxIndexEqualsValue(array, target, start, end, get_min=False, get_max=False):
    res = -1
    while start <= end:
        mid = (end - start) // 2 + start
        if array[mid] == target:
            res = mid
            if get_min:
                end = mid - 1
            elif get_max:
                start = mid + 1
            else:
                return res
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return res


def searchForRange(array, target):
    start, end = 0, len(array) - 1
    mid_index = minOrMaxIndexEqualsValue(array, target, start, end)
    min_index = minOrMaxIndexEqualsValue(array, target, start, mid_index, get_min=True)
    max_index = minOrMaxIndexEqualsValue(array, target, mid_index, end, get_max=True)
    return [min_index, max_index]


if __name__ == '__main__':
    print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
