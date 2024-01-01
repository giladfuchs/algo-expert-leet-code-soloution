def commonCharacters(strings):
    res = set(strings.pop())
    for _ in strings:
        res = res.intersection(set(_))
    return list(res)


def nonConstructibleChange(coins):
    min_change = 0
    coins.sort()
    for coin in coins:
        if coin > min_change + 1:
            break
        min_change += coin
    return min_change + 1


if __name__ == '__main__':
    print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
    # print(commonCharacters(["abc", "bcd", "cbad"]))
