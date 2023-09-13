def numbersInPi(pi, numbers):
    numbers.sort(key=len, reverse=True)
    temp_pi: str = pi
    max_count = float('inf')
    for i in range(numbers):
        count = -1
        for _ in numbers:
            if _ in temp_pi:
                temp_pi = temp_pi.replace(_, '')
                count += 1
        print(count)
        if count > 0 and count < max_count:
            max_count = count
    # Write your code here.
    return max_count


if __name__ == '__main__':
    print(numbersInPi('3141592653589793238462643383279',
                      ['314159265358979323846', '35897932384626433832', '314159265', '26433', '3279', '79', '8']))
