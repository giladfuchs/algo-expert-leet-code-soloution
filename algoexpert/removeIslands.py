import pprint


def traverse_islands(i, j, matrix, is_edge):
    if matrix[i][j] != 1:
        return
    matrix[i][j] = 2 if is_edge else 0
    if i > 0:
        traverse_islands(i - 1, j, matrix, is_edge)
    if j > 0:
        traverse_islands(i, j - 1, matrix, is_edge)
    if i < len(matrix) - 1:
        traverse_islands(i + 1, j, matrix, is_edge)
    if j < len(matrix[0]) - 1:
        traverse_islands(i, j + 1, matrix, is_edge)


def removeIslands(matrix):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                traverse_islands(i, j, matrix, True)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            traverse_islands(i, j, matrix, False)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                matrix[i][j] = 1
    return matrix


if __name__ == '__main__':
    pprint.pprint(removeIslands([
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]))
