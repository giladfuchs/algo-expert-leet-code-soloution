def threeNumberSort(array, order):
    index = 0
    for i in range(2):
        val = order[i]
        for j in range(len(array)):
            if array[j] == val:
                array[index], array[j] = array[j], array[index]
                index += 1
    return array


print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
