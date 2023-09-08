def longestPeak(array):
    size = len(array)
    i = 1
    ans = 0
    while i < size-1:
        if not (array[i-1]< array[i] and array[i+1] < array[i]):
            i += 1
        else:
            left = i-2
            while left>-1 and array[left] < array[left+1]:
                left-=1
            right = i + 2
            while right<size and array[right-1] > array[right]:
                right+=1
            temp = right-left-1
            ans = max(temp, ans)
            i = right

    return ans
print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
