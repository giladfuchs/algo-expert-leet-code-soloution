def bestSeat(seats):
    temp = 0
    _max = 0
    index = -1
    for i in range(len(seats)):
        if seats[i]:
            if temp > _max:
                _max = temp
                index = i - 1 - temp // 2
            temp = 0
        else:

            temp += 1

    return index


if __name__ == '__main__':
    print(bestSeat([1, 0, 1, 0, 0, 0, 1]))
