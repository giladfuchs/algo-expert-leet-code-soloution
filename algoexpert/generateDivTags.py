def rec_create_div(prefix, opening, close, divs):
    if not close:
        divs.append(prefix)
    if opening:
        rec_create_div(f'{prefix}<div>', opening - 1, close, divs)
    if opening < close:
        rec_create_div(f'{prefix}</div>', opening, close - 1, divs)
    return divs


def generateDivTags(numberOfTags):
    return rec_create_div('', numberOfTags, numberOfTags, [])


if __name__ == '__main__':
    print(generateDivTags(3))
