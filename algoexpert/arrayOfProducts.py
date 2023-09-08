def arrayOfProducts(array):
    n = len(array)
    mul_array = [1] * n
    mul_array2 = [1] * n
    for i in range(1, n):
        mul_array[i] = mul_array[i - 1] * array[i - 1]
    for i in range(n - 2, -1,-1):
        mul_array2[i] = mul_array2[i + 1] * array[i + 1]

    array[0] = mul_array2[0]
    array[n - 1] = mul_array[n - 1]

    for i in range(n - 1):
        array[i] = mul_array2[i ] * mul_array[i ]
    return array

arrayOfProducts([5, 1, 4, 2])