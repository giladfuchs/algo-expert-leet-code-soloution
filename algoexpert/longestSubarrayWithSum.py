def longestSubarrayWithSum(array, targetSum):
    if targetSum ==0:
        index = array.index(0)
        return [index,index]
    left = [0]
    right = [0]
    for _ in array:
        left.append(left[-1] + _)
    for _ in array[::-1]:
        right.append(right[-1] + _)
    # left1 = left[::-1]
    right = right[::-1]
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        cur = right[right_index] - left[left_index]
        if cur == targetSum:
            break
        if cur > targetSum:
            left_index += 1
        else:
            right_index += 1
    if left_index > len(array) - right_index - 1:
        return []
    return [left_index, len(array) - right_index - 1]


if __name__ == '__main__':
    print(longestSubarrayWithSum( [1, 4, 10, 15, 31, 7, 1, 40, 0, 20, 1, 1, 1, 1, 2, 1],  0))
