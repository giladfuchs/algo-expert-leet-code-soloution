def numberOfWaysToMakeChange(n, denoms):
    ways_to_make_change = [1] + [0 for _ in range(n)]
    for denom in denoms:
        for change in range(denom, n +1):
            ways_to_make_change[change] += ways_to_make_change[change-denom]
    return ways_to_make_change[-1]


if __name__ == '__main__':
    print(numberOfWaysToMakeChange(10, [1, 5, 10, 25]))