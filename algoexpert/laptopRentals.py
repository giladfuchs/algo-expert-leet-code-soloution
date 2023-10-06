def laptopRentals(times):
    if not times:
        return 0
    times.sort(key=lambda x: x[0])
    res = [times.pop(0)[1]]
    for start, end in times:
        res.sort()
        if start >= res[0]:
            res[0] = end
        else:
            res.append(end)
    return len(res)


if __name__ == '__main__':
    print(laptopRentals([
        [0, 2],
        [1, 4],
        [4, 6],
        [0, 4],
        [7, 8],
        [9, 11],
        [3, 10]
    ]))
