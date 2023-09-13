def validStartingCity(distances, fuel, mpg):
    cur_gas, res = 0, -1
    for i in range(len(distances)):
        cur_gas += fuel[i] * mpg
        if cur_gas >= 0 and res == -1:
            res = i
        cur_gas -= distances[i]
        if cur_gas < 0:
            res = -1
            cur_gas = 0
    return res


if __name__ == '__main__':
    b = validStartingCity([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10)
    print(b)
