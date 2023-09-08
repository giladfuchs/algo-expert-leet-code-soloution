# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    ans = 0
    mul, i = 1, 1
    temp_array = []

    while temp_array or array:
        while array:
            temp = array.pop()
            if isinstance(temp, int):
                ans += temp * mul
            else:
                temp_array += temp
        array = temp_array
        temp_array = []
        i += 1
        mul *= i

    return ans

if __name__ == '__main__':
    # print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
    print(productSum([9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7],
                      [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
                      [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]))
