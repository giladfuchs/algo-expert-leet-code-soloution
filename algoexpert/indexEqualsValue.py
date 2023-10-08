def indexEqualsValue(array):
    start, end = 0, len(array) - 1
    res = -1
    while start <= end:
        mid = (end - start) // 2 + start
        if array[mid] == mid:
            res = mid
            end = mid - 1
        if array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1

    return res


if __name__ == '__main__':
    print(indexEqualsValue([0,1,2,3,4]))
