def knapsackProblem(items, capacity):
    n = len(items) + 1
    mat = [[0] * (capacity + 1) for i in range(n)]
    for i in range(1, n):
        for j in range(0, capacity + 1):

            if items[i - 1][1] > j:
                mat[i][j] = mat[i - 1][j]
            else:
                temp = mat[i - 1][j - items[i - 1][1]] + items[i - 1][0]

                mat[i][j] = max(temp, mat[i - 1][j])

    index = n - 1
    ans = []
    while index > 0 and capacity > 0:
        if mat[index][capacity] == mat[index - 1][capacity]:
            index -= 1
        else:
            ans.append(index - 1)
            capacity -= items[index - 1][1]
            index -= 1

    return [mat[-1][-1], ans]




if __name__ == '__main__':
    print(knapsackProblem([
        [1, 2],
        [4, 3],
        [5, 6],
        [6, 7]
    ], 10))
