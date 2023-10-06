def sunsetViews(buildings, direction):
    res = []
    temp_max = 0

    n = len(buildings)

    for i in range(n-1, -1, -1) if direction == 'EAST' else range(n):
        if buildings[i] > temp_max:
            res.append(i)
            temp_max = buildings[i]
    res.sort()
    return res


if __name__ == '__main__':
    print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], 'EAST'))
