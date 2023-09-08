def subarraySort(array):
    ans = [-1,-1]
    mm = 0
    i = 0
    no_order = []
    while i< len(array):
        if array[i]>=mm:
            mm=array[i]
        else:
            no_order.append(i)
        i+=1
    if not no_order:
        return ans
    min_num = min([array[_] for _ in no_order])
    i = 0
    while i<len(array):
        if array[i]<min_num:
            i+=1
        else:
            break
    ans[0] = i
    ans[1] = max(no_order)
    return ans


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))