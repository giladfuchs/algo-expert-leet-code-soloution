import random


def paint(arr):
    count = arr[-1]
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            count += arr[i - 1] - arr[i]
            if count > 1000000000:
                return -1
    return count


def sort_zero_and_one(arr):
    random.shuffle(arr)
    pos = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        while pos > i and arr[pos] == 1: pos -= 1
        if pos < i:
            break
        arr[i], arr[pos] = arr[pos], arr[i]
    return arr


print(sort_zero_and_one([_ % 2 for _ in range(20)]))
#
# print(paint([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))
# print(paint([5, 8]))
# print(paint([1,1,1,1]))
