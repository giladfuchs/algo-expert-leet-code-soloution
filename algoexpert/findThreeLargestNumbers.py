def findThreeLargestNumbers(array):
    if len(array) < 4:
        return array
    maxes = array[:3]
    maxes.sort()
    for num in array[3:]:
        if num>maxes[0]:
            maxes[0] = num
            maxes.sort()

    return maxes


if __name__ == '__main__':
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
