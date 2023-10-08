def juiceBottling2(prices):
    n = len(prices)
    mat = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i > j:
                mat[i][j] = 0
            else:
                remain = [mat[k][j - 1] for k in range(i + 1)]
                mat[i][j] = prices[i] + max(remain)

    maxi = 0
    ind = [0, 0]
    for i in range(n):
        temp = max(mat[i])
        if temp > maxi:
            maxi = temp
            ind = [i, mat[i].index(temp)]
    index = [ind[0]]
    remain = ind[1] - ind[0]
    while remain > 0:
        nxt = remain
        col = [mat[k][nxt] for k in range(n)]
        maxi = max(col)
        ind = col.index(maxi)
        index.append(ind)
        remain -= ind
    return sorted(index)


def juiceBottling(prices):
    num_sizes = len(prices)
    max_profit = [0] * num_sizes
    solution = [[]] * num_sizes
    for size in prices:
        for dividing_point in range(size + 1):
            possible_profit = max_profit[size - dividing_point] + prices[dividing_point]
            if possible_profit > max_profit[size]:
                max_profit[size] = possible_profit
                solution[size] = [dividing_point] + solution[size - dividing_point]

    return solution[-1]


if __name__ == '__main__':
    print(juiceBottling([0, 1, 3, 2]))
