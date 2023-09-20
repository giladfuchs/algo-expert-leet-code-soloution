small = lambda arr, head: [_ for _ in arr if _ < head]
big = lambda arr, head: [_ for _ in arr if _ >= head]


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if not arrayTwo:
        return True

    head1, head2 = arrayOne.pop(0), arrayTwo.pop(0)
    if head1 != head2:
        return False

    left1 = small(arrayOne, head1)
    left2 = small(arrayTwo, head2)
    right1 = big(arrayOne, head1)
    right2 = big(arrayTwo, head2)
    return sameBsts(left1, left2) and sameBsts(right1, right2)


if __name__ == '__main__':
    print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))
