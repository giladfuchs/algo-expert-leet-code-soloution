def binarySearch(array, target):
    start, end = 0, len(array)

    while start < end:
        mid = (end - start) // 2 + start
        if target == array[mid]:
            return mid
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
    return -1


def binarySearchLower(array, target):
    start, end = 0, len(array)-1

    ans = 0
    while start < end :
        mid = (end - start) // 2 + start
        if array[mid] >= target:
            end = mid-1
        else:
            start = mid + 1
            ans = mid
    return array[ans]


if __name__ == '__main__':
    # print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
    # print(binarySearch([1, 5, 23, 111], 33))
    # print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],1))
    print(binarySearchLower([1,7], 3))
