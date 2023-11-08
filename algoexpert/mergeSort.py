
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)

        i_left = i_right = k = 0
        while i_left < len(left) and i_right < len(right):
            if left[i_left] < right[i_right]:
                array[k] = left[i_left]
                i_left += 1
            else:
                array[k] = right[i_right]
                i_right += 1

            k += 1
        while i_left < len(left):
            array[k] = left[i_left]
            i_left += 1
            k += 1
        while i_right < len(right):
            array[k] = right[i_right]
            i_right += 1
            k += 1


if __name__ == '__main__':
    arr_test = [_ for _ in range(22)]
    import random

    random.shuffle(arr_test)
    mergeSort(arr_test)
    print(arr_test)
