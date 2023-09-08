# def largestRange(array):
#     diff = lambda arr: arr[1] - arr[0]
#     array.sort()
#     _min = array[0]
#     _max = array[0]
#     ans = [_min, _max]
#     n = len(array)-1
#     i = 0
#     while i<n:
#         _min = array[i]
#
#         while i<n and array[i]>= array[i+1]-1:
#             _max = array[i+1]
#             i += 1
#         ans = max(ans, [_min, _max], key=diff)
#         i+=1
#     return ans
def largestRange(array):
    diff = lambda arr: arr[1] - arr[0]
    _set = set(array)
    ans = [array[0], array[0]]
    for _ in array:
        if _ in _set:
            left = right = _
            while (left -1) in _set:
                left-=1
                _set.discard(left)
            while (right +1) in _set:
                right+=1
                _set.discard(right)
            ans = max(ans, [left, right], key=diff)


    return ans

print(largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
# print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))