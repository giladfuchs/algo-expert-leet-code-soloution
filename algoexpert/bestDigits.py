def bestDigits(number, numDigits):
    if numDigits == 0:
        return number
    if numDigits > 1:
        temp_number = number[:numDigits * 2]
        rest_number = number[numDigits * 2:]
    else:
        temp_number = number
        rest_number = ''
    max_temp = max(temp_number[:len(temp_number) // 2 + 1])
    index_max_temp = temp_number.index(max_temp)
    numDigits -= index_max_temp
    temp_number = temp_number[index_max_temp:]
    for _ in range(numDigits):
        min_temp = min(temp_number)
        index_min_temp = temp_number.index(min_temp)
        temp_number = temp_number[:index_min_temp] + temp_number[index_min_temp + 1:]
    return temp_number + rest_number


if __name__ == '__main__':
    print(bestDigits("1020304050", 5))
