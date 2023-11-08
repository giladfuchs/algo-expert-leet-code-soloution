def paint(arr):
    count = arr[-1]
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            count += arr[i - 1] - arr[i]
            if count > 1000000000:
                return -1
    return count


print(paint([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))
print(paint([5, 8]))
print(paint([1,1,1,1]))
