size = 4
def rectangleMania(coords):
    mat = [[False] * size for _ in range(size)]
    for i, j in coords:
        mat[i][j] = True
    return mat


if __name__ == '__main__':
    print(rectangleMania([
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0],
        [3, 1],
        [3, 0]
    ]))
