def zigzagTraverse(array):
    n, m = len(array), len(array[0])
    ans = []
    up_way = False
    i, j = 0, 0

    while i < n and j < m:
        ans.append(array[i][j])
        if up_way:
            if j == m - 1:
                up_way = False
                i += 1
            elif i == 0:
                up_way = False
                j += 1
            else:
                i -= 1
                j += 1
        else:
            if i == n - 1:
                up_way = True
                j += 1
            elif j == 0:
                up_way = True
                i += 1
            else:
                i += 1
                j -= 1
    return ans


if __name__ == '__main__':
    print(zigzagTraverse([[1, 3, 4, 10, 11, 20],
                          [2, 5, 9, 12, 19, 21],
                          [6, 8, 13, 18, 22, 27],
                          [7, 14, 17, 23, 26, 28],
                          [15, 16, 24, 25, 29, 30]]))
