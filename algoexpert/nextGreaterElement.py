def nextGreaterElement2(array):
    # Write your code here.
    res = []
    find_greater = lambda x, arr: next((val for val in arr
                                        if val > x), -1)
    for i, num in enumerate(array):
        temp = array[i:len(array)] + array[0:i]
        res.append(find_greater(num, temp))

    return res


def nextGreaterElement(array):
    n = len(array)
    res = [-1] * n
    st = []

    for i in range(n * 2 - 1, -1, -1):
        idx = i % n
        while st:
            if st[-1] <= array[idx]:
                st.pop()
            else:
                res[idx] = st[-1]
                break
        st.append(array[idx])

    return res


if __name__ == '__main__':
    print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))
