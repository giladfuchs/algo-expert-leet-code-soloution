def commonCharacters(strings):
    res = set(strings.pop())
    for _ in strings:
        res = res.intersection(set(_))
    return list(res)


if __name__ == '__main__':
    print(commonCharacters(["abc", "bcd", "cbad"]))
