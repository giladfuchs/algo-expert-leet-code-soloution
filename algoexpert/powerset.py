import math


def powerset(array):
    sets = []

    def helperPowerSet(index, subset):
        if index == len(array):
            sets.append(subset[:])
            return

        helperPowerSet(index + 1, subset)
        subset.append(array[index])
        helperPowerSet(index + 1, subset)
        subset.pop()

    helperPowerSet(0, [])
    return sets


def powerset_of_k(array, k):
    sets = []
    n = len(array)

    def helperPowerSetOfK(temp):
        subset = []
        for _ in range(k):
            subset.append(array[temp % n])
            temp //= n
        sets.append(subset[:])

    for i in range(int(math.pow(k, n))):
        helperPowerSetOfK(i)

    return sets


if __name__ == '__main__':
    # print(powerset([1, 2, 3]))
    print(powerset_of_k([1, 2, 3],2))
