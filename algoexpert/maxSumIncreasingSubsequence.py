def maxSumIncreasingSubsequenceMy(array):
    n = len(array)
    temp = [0] * n
    find_index = lambda ran, number: next((index for index in range(ran - 1, -1, -1) if array[index] < number), ran)
    for i, num in enumerate(array):
        index = find_index(i, num)
        temp[i] = num + (temp[index] if temp[index] > 0 else 0)
    peak_num = max(temp)
    peak_index = temp.index(peak_num)
    temp_index = peak_index
    peak_array = [array[peak_index]]
    while sum(peak_array) != peak_num:
        temp_index -= 1
        if array[temp_index] < array[peak_index]:
            peak_array.append(array[temp_index])
            peak_index = temp_index
    return [peak_num, peak_array[::-1]]


def maxSumIncreasingSubsequence(array):
    n = len(array)
    seqs = [None] * n
    sums = array[:]
    for i, cur in enumerate(array):
        for j in range(i):
            other_num = array[j]
            if other_num < cur and sums[j] + cur >= sums[i]:
                sums[i] = sums[j] + cur
                seqs[i] = j

    peak_num = max(sums)
    peak_index = sums.index(peak_num)
    res_seq = []
    while seqs[peak_index] is not None:
        res_seq.append(array[peak_index])
        peak_index = seqs[peak_index]
    res_seq.append(array[peak_index])

    return [peak_num, res_seq[::-1]]


print(maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]))
# print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
