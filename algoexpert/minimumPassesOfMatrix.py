position_to_check = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]


def minimumPassesOfMatrix(matrix):
    n, m = len(matrix), len(matrix[0])
    ans = -1
    positive_position = []
    count = 0

    for row in range(n):
        for col in range(m):
            if matrix[row][col] >= 0:
                count += 1

            if matrix[row][col] > 0:
                positive_position.append([row, col])
    while True:
        ans += 1
        if not positive_position:
            return ans - 1 if count == n*m else -1
        temp_position = []

        while positive_position:

            row, col = positive_position.pop(0)

            for i, j in position_to_check:
                temp_row = row + i
                temp_col = col + j
                if temp_row < n and temp_row >= 0 and \
                        temp_col < m and temp_col >= 0 and \
                        matrix[temp_row][temp_col] < 0:
                    matrix[temp_row][temp_col] *= -1
                    temp_position.append([temp_row, temp_col])
                    count += 1
        positive_position = temp_position


if __name__ == '__main__':
    print(minimumPassesOfMatrix([
        [-1, -9, 0, -1, 0],
        [-9, -4, -5, 4, -8],
        [2, 0, 0, -3, 0],
        [0, -17, -4, 2, -5]
    ]))
