def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    n = len(redShirtHeights)
    i = 0
    while i < n:
        if redShirtHeights[i] < blueShirtHeights[i]:
            i += 1
        else:
            break
    if i == n:
        return True
    i = 0
    while i < n:
        if redShirtHeights[i] > blueShirtHeights[i]:
            i += 1
        else:
            break
    if i == n:
        return True
    return False


print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
