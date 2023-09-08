def kadanesAlgorithm(array):
    max_count, temp = -float('inf'), 0
    for _ in array:
        temp += _
        if temp >= max_count:
            max_count = temp
        if temp < 0:
            temp = 0
    return max_count


if __name__ == '__main__':
    print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
