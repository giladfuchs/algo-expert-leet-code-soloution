def reversePolishNotation(tokens):
    st = []
    res = 0
    for t in tokens:
        if t in ['/', '*', '+', '-']:
            num1 = st.pop()
            num2 = st.pop()
            if t == '/':
                num2 /= num1
            elif t == '*':
                num2 *= num1
            elif t == '+':
                num2 += num1
            elif t == '-':
                num2 -= num1
            st.append(int(num2))
        else:
            st.append(int(t))
    return int(st[-1])


def majorityElement(array):
    res = array[0]
    count = 1
    for num in array[1:]:
        if num == res:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = num
            count = 1
    return res


def collidingAsteroids(asteroids):
    st = []
    for ast in asteroids:
        if ast > 0:
            st.append(ast)
            continue

        while True:
            if not st or st[-1] < 0:
                st.append(ast)
                break

            abs_ast = abs(ast)
            if st[-1] > abs_ast:
                break
            if st[-1] == abs_ast:
                st.pop()
                break
            st.pop()

    return st


# print(reversePolishNotation(["4", "-7", "2", "6", "+", "10", "-", "/", "*", "2", "+", "3", "*"]))
def moveElementToEnd(array, toMove):
    start, end = 0, len(array) - 1

    while start < end:
        while start < end and array[end] == toMove:
            end -= 1
        if array[start] == toMove:
            array[start], array[end] = array[end], array[start]
            end -= 1
        start += 1
    return array


# print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
def zeroSumSubarray(nums):
    sums = set([0])
    curr = 0
    for num in nums:
        curr += num
        if curr in sums:
            return True
        sums.add(curr)
    return False

print(zeroSumSubarray([-5, -5, 2,1, 3, -2]))