def order_check(arr):
    temp = sorted(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i]!=temp[i]:
            count+=1
    return count


print(order_check([1, 1, 3, 3, 4, 1]))
print(order_check([1, 1, 3, 4, 1]))
