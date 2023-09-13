def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=True if fastest else False)
    res = 0

    while redShirtSpeeds:
        res += max(redShirtSpeeds.pop(), blueShirtSpeeds.pop())

    return res


if __name__ == '__main__':
    print(tandemBicycle([5, 5, 3, 9, 2],[3, 6, 7, 2, 1], True))
    print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
