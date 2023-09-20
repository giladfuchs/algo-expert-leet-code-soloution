def getPermutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            getPermutationsHelper(i + 1, array, permutations)
            array[i], array[j] = array[j], array[i]


def getPermutations(array):
    permutations = []
    getPermutationsHelper(0, array, permutations)
    return permutations

if __name__ == '__main__':
    print(getPermutations([1, 2, 3]))