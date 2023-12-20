def maxSubsetSumNoAdjacent2(array):
    array_len = len(array)
    if array_len < 3:
        return max(array) if array else 0
    temp = [0] * array_len
    temp[0], temp[1], temp[2] = array[0], array[1], array[2] + array[0]
    for i in range(3, array_len):
        temp[i] = max(temp[i - 2], temp[i - 3]) + array[i]

    return max(temp)
def maxSubsetSumNoAdjacent(array):
    prev, cur = 0, 0
    for num in array:
        prev, cur= cur, max(cur, prev+num)
    return cur

if __name__ == '__main__':
    print(maxSubsetSumNoAdjacent([75, 105, 120, 91, 90, 135]))
