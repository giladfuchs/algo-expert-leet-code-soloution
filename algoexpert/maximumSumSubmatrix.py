def maximumSumSubmatrix(matrix, size):
    sums = [[0 for i in range(len(matrix[0]))] for _ in matrix]
    res = float('-inf')
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if all(ele == 0 for ele in [row, col]):
                sums[row][col] = matrix[row][col]
            elif row == 0:
                sums[row][col] = matrix[row][col] + sums[row][col - 1]
            elif col == 0:
                sums[row][col] = matrix[row][col] + sums[row - 1][col]
            else:
                sums[row][col] = matrix[row][col] + sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1]
            temp = float('-inf')

            if row + 1 >= size and col + 1 >= size:
                temp = sums[row][col]
            if row >= size:
                temp -= sums[row - size][col]
            if col >= size:
                temp -= sums[row][col - size]
            if row >= size and col >= size:
                temp += sums[row - size][col - size]
            res = max(res, temp)
    return res
